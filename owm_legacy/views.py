import swapper
from django.shortcuts import get_object_or_404

from openwisp_controller.config.controller.views import UpdateLastIpMixin
from openwisp_controller.config.signals import checksum_requested
from openwisp_controller.config.utils import send_device_config, send_file

from .utils import forbid_unallowed

Device = swapper.load_model('config', 'Device')
Config = swapper.load_model('config', 'Config')
ip_updater = UpdateLastIpMixin()
ip_updater.model = Device


def get_config_md5(request, mac_address):
    """
    returns md5 of configuration
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, device__mac_address__iexact=mac_address)
    # in OpenWISP 1, the last_ip field and the management_ip are the same
    # because the config is downloaded via the management VPN
    request.GET = {'management_ip': request.META.get('REMOTE_ADDR')}
    ip_updater.update_last_ip(config.device, request)
    # send checksum_requested signal
    checksum_requested.send(
        sender=config.device.__class__, instance=config.device, request=request
    )
    return send_file(mac_address, config.get_cached_checksum())


def get_config(request, mac_address):
    """
    returns configuration tar.gz
    """
    forbid_unallowed(request)
    config = get_object_or_404(Config, device__mac_address__iexact=mac_address)
    config.set_status_applied()
    return send_device_config(config, request)
