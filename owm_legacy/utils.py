import ipaddress
import logging

from django.core.exceptions import PermissionDenied

from .settings import ALLOWED_SUBNETS

logger = logging.getLogger(__name__)


def ip_allowed(address_string):
    """
    returns ``True`` if specified ip address is allowed
    according to ``settings.OWM_LEGACY_ALLOWED_SUBNETS``
    otherwise returns ``False``
    """
    ip_address = ipaddress.ip_address(address_string)
    for subnet_string in ALLOWED_SUBNETS:
        network = ipaddress.ip_network(subnet_string)
        if ip_address in network:
            return True
    return False


def forbid_unallowed(request):
    """
    raises ``PermissionDenied`` if remote address is not allowed
    """
    if not ip_allowed(request.META.get('REMOTE_ADDR')):
        logger.warning('PermissionDenied', extra={'request': request, 'stack': True})
        raise PermissionDenied
