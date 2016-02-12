from django.shortcuts import get_object_or_404

from django_netjsonconfig.models import Config
from django_netjsonconfig.utils import send_config, send_file, update_last_ip

from .utils import forbid_unallowed


def get_config_md5(request, key):
    """
    returns md5 of configuration bytes
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, key__iexact=key)
    update_last_ip(config, request)
    return send_file(key, config.checksum)


def get_config(request, key):
    """
    returns md5 of configuration bytes
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, key__iexact=key)
    config.status = 'running'
    return send_config(config, request)
