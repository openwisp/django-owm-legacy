from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('owm_legacy.urls', namespace='owm_legacy')),
    url(r'', include('openwisp_controller.urls')),
]

urlpatterns += staticfiles_urlpatterns()
