import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': 'owm-legacy.db',
    }
}

SECRET_KEY = 'fn)t*+$)ugeyip6-#txyy$5wf2ervc0d2n#h)qb)y5@ly$t*@w'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    # allauth
    'allauth',
    'allauth.account',
    'django_extensions',
    # openwisp2 modules
    'openwisp_controller.config',
    'openwisp_controller.pki',
    'openwisp_controller.geo',
    'openwisp_controller.connection',
    'openwisp_users',
    # openwisp2 admin theme
    # (must be loaded here)
    'openwisp_utils.admin_theme',
    'django.contrib.admin',
    'django.forms',
    # other dependencies
    'sortedm2m',
    'reversion',
    'leaflet',
    'flat_json_widget',
    'owm_legacy',
]


EXTENDED_APPS = ('django_x509', 'django_loci')

AUTH_USER_MODEL = 'openwisp_users.User'
SITE_ID = 1

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'openwisp_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'openwisp2.urls'

TIME_ZONE = 'Europe/Rome'
LANGUAGE_CODE = 'en-gb'
USE_TZ = True
USE_I18N = False
USE_L10N = False
STATIC_URL = '/static/'
CORS_ORIGIN_ALLOW_ALL = True


ASGI_APPLICATION = 'openwisp_controller.geo.channels.routing.channel_routing'
CHANNEL_LAYERS = {
    # in production you should use another channel layer backend
    'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'},
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'openwisp_utils.loaders.DependencyLoader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'openwisp_utils.admin_theme.context_processor.menu_items',
                'openwisp_notifications.context_processors.notification_api_settings',
            ],
        },
    }
]

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost/0',
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient',},
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

CELERY_BROKER_URL = 'redis://localhost/1'

# Workaround for stalled migrate command
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'max_retries': 10,
}


# local settings must be imported before test runner
# otherwise they'll be ignored
try:
    from local_settings import *
except ImportError:
    pass
