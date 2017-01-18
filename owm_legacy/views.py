from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ImproperlyConfigured

if 'django_netjsonconfig' in settings.INSTALLED_APPS:
    from django_netjsonconfig.models import Config
elif 'openwisp2.config' in settings.INSTALLED_APPS:  # pragma: nocover
    from openwisp2.config.models import Config
else:  # pragma: nocover
    raise ImproperlyConfigured('django-owm-legacy depends on django-netjsonconfig or '
                               'openwisp2.config, but neither of the two is present '
                               'in settings.INSTALLED_APPS')

from django_netjsonconfig.controller.generics import BaseConfigView
from django_netjsonconfig.utils import send_config, send_file, update_last_ip

from .utils import forbid_unallowed


def get_config_md5(request, mac_address):
    """
    returns md5 of configuration
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, mac_address__iexact=mac_address)
    update_last_ip(config, request)
    return send_file(mac_address, config.checksum)


def get_config(request, mac_address):
    """
    returns configuration tar.gz
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, mac_address__iexact=mac_address)
    config.status = 'running'
    return send_config(config, request)
