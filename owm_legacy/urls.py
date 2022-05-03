from django.urls import re_path

from . import views

app_name = "owm_legacy"

urlpatterns = [
    re_path(
        r'^get_config/(?P<mac_address>[^/^.]+).md5$',
        views.get_config_md5,
        name='get_config_md5',
    ),
    re_path(
        r'^get_config/(?P<mac_address>[^/^.]+)$', views.get_config, name='get_config'
    ),
    # support aliases for OWM
    re_path(
        r'^owm/get_config/(?P<mac_address>[^/^.]+).md5$',
        views.get_config_md5,
        name='owm_get_config_md5',
    ),
    re_path(
        r'^owm/get_config/(?P<mac_address>[^/^.]+)$',
        views.get_config,
        name='owm_get_config',
    ),
]
