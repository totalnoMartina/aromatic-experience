from pathlib import Path
import os
import sys
import dj_database_url
from django.contrib.messages import constants as messages
if os.path.isfile('env.py'):
    import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False


X_FRAME_OPTIONS = 'SAMEORIGIN'  # The page can be displayed in a frame of same origin

ALLOWED_HOSTS = ['aromatic-martina.herokuapp.com', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'crispy_forms',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'django_summernote',
    # My apps
    'aromaticblog',
]

SITE_ID = 1
CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'

ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# For details about facebook social account connecting
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_EU',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}

SOCIAL_AUTH_FACEBOOK_ID = os.environ.get("SOCIAL_AUTH_FACEBOOK_ID")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aromaticproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'allauth', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # For media files
                                                             # in dev and pro
            ],
        },
    },
]

WSGI_APPLICATION = 'aromaticproject.wsgi.application'

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
elif 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
