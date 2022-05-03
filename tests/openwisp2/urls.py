from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('openwisp_controller.urls')),
    path('', include('owm_legacy.urls', namespace='owm_legacy')),
]

urlpatterns += staticfiles_urlpatterns()
