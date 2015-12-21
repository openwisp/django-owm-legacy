from django.conf import settings

ALLOWED_SUBNETS = getattr(settings, 'OWM_LEGACY_ALLOWED_SUBNETS', ['10.8.0.0/16',
                                                                   '127.0.0.1/32'])
