import os
import datetime
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'VERY_SECRET_KEY_THAT_YOU_SHOULD_CHANGE')

ROOT_URLCONF = 'ams.urls'
SITE_ID = 1

# used for email confirmation
PASSWORD_RESET_TIMEOUT_DAYS = 7

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',

    'svg',
    'sass_processor',
    'captcha',

    'ams.modules.petition',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Localization
LANGUAGE_CODE = 'de'
TIME_ZONE = 'Europe/Vienna'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
  ('de', 'Deutsch - German'),
  ('en', 'English - Englisch'),
  ('fr', 'français - Französisch'),
  ('sr', 'српски - Serbisch'),
  ('bs', 'bosanski - Bosnisch'),
  ('hr', 'hrvatski - Kroatisch'),
  ('uk', 'українська мова - Ukainisch'),
  ('tr', 'Türkçe - Türkisch'),
  ('cs', 'čeština - Tschechisch'),
  ('ar', 'اَلْعَرَبِيَّة - Arabisch'),
  ('fa', 'Fārsī - Persisch'),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

RUN_DIR = os.path.join(BASE_DIR, '../run')

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(RUN_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'static/scss'),
    os.path.join(BASE_DIR, '../node_modules'),
]

SVG_DIRS=[
    os.path.join(BASE_DIR, 'static/svg'),
]

# Captcha settings
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS = ()
CAPTCHA_LETTER_ROTATION = None
CAPTCHA_MATH_CHALLENGE_OPERATOR = 'x'
CAPTCHA_FOREGROUND_COLOR = '#fff'
CAPTCHA_BACKGROUND_COLOR = 'rgb(59, 64, 83)'
