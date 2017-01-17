from django.shortcuts import get_object_or_404

from django_netjsonconfig.models import Config
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
