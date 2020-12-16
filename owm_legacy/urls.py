from django.conf.urls import url

from . import views

app_name = "owm_legacy"

urlpatterns = [
    url(
        r'^get_config/(?P<mac_address>[^/^.]+).md5$',
        views.get_config_md5,
        name='get_config_md5',
    ),
    url(r'^get_config/(?P<mac_address>[^/^.]+)$', views.get_config, name='get_config'),
]
