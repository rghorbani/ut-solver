"""
Django settings for ut_solver project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODE = 'development'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g+9d8!3r4n$d1xvge#8ac=pzfm3oh1^4-+9#eyz5$@lc3mwoeh'

# SECURITY WARNING: don't run with debug turned on in production!
if MODE == 'development':
    DEBUG = TEMPLATE_DEBUG = True
else:
    DEBUG = TEMPLATE_DEBUG = False

ADMINS = (('Reza', 'r.ghorbani.f@gmail.com'),)

ALLOWED_HOSTS = [
    '*'
]


# Application definition

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'djcelery',
    'kombu.transport.django',
    'jinja2',
    'numpy',
    'matplotlib',
    'mpld3',
)

LOCAL_APPS = (
    'frontend',
    'lex',
    'lexer',
    'optimization',
    'simplex',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ut_solver.urls'

import djcelery
BROKER_URL = 'django://'
djcelery.setup_loader()

WSGI_APPLICATION = 'ut_solver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'solver',
        'USER': 'solver',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'America/New_York'
TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ut.solver00'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'ut.solver00'
DEFAULT_TO_EMAIL = 'r.ghorbani.f@gmail.com'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Production
# http://stackoverflow.com/questions/4420378/why-my-django-admin-site-does-not-have-the-css-style
# use this command 'mysite.com/app_folder/static$ sudo ln -s /usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin/ admin'
STATIC_ROOT = ''
STATIC_URL = '/static/'

LOGIN_URL = '/users/sign_in/'

LOGIN_REDIRECT_URL = '/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'