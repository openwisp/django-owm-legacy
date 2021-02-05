import swapper
from django.shortcuts import get_object_or_404

from openwisp_controller.config.utils import (
    send_device_config,
    send_file,
    update_last_ip,
)

from .utils import forbid_unallowed

Device = swapper.load_model('config', 'Device')
Config = swapper.load_model('config', 'Config')


def get_config_md5(request, mac_address):
    """
    returns md5 of configuration
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, device__mac_address__iexact=mac_address)
    update_last_ip(config.device, request)
    return send_file(mac_address, config.checksum)


def get_config(request, mac_address):
    """
    returns configuration tar.gz
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, device__mac_address__iexact=mac_address)
    config.set_status_applied()
    return send_device_config(config, request)
