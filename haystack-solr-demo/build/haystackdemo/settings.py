import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'errors@hipo.biz'
DEFAULT_FROM_EMAIL = 'no-reply@hipo.biz'

ADMINS = (
    ('Taylan Pince', 'taylan@hipo.biz'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/files')
STATIC_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/static')

SECRET_KEY = '$7h91tuu7)233mqzp56+i)6^)(xv8hy_sdopqup9s(0nzbedsn'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'haystackdemo.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates/'),
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'haystackdemo',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

    'django_extensions',
    'haystack',
    'south',

    'articles',
)

HAYSTACK_SITECONF = 'haystackdemo.search_sites'
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr/haystack_demo'

try:
    from settings_local import *
except:
    pass

MEDIA_URL = ROOT_MEDIA_URL + '/media/'
STATIC_URL = ROOT_MEDIA_URL + '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
