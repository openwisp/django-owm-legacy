import hashlib

from django.shortcuts import get_object_or_404
from django_netjsonconfig.models import Device
from django_netjsonconfig.utils import send_file

from .utils import forbid_unallowed


def get_config_md5(request, key):
    """
    returns md5 of configuration bytes
    """
    forbid_unallowed(request)
    device = get_object_or_404(Device, key__iexact=key)
    config = device.backend_instance.generate()
    md5 = hashlib.md5(config.getvalue()).hexdigest()
    return send_file(key, md5)


def get_config(request, key):
    """
    returns md5 of configuration bytes
    """
    forbid_unallowed(request)
    device = get_object_or_404(Device, key__iexact=key)
    config = device.backend_instance.generate()
    return send_file(filename='{0}.tar.gz'.format(device.name),
                     contents=config.getvalue())
