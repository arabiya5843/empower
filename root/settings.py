import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

from shared.django import os_environ_get

# Load env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os_environ_get('DJANGO_SECRET_KEY')

DEBUG = os_environ_get('DEBUG')

ALLOWED_HOSTS = ['3002']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'apps.ai_supportive',
    'apps.users',       # Custom user model and user-related functionality
    'apps.employment',  # Functionality related to job vacancies, responsibilities, etc.
    'apps.orders',      # Functionality related to user cards and orders

    # Third party apps
    'rest_framework',           # Django Rest Framework for building APIs
    'rest_framework_simplejwt',  # JWT-based authentication for Django Rest Framework
    'drf_yasg',                 # Yet Another Swagger Generator for Django Rest Framework
    'django_filters',           # Filter support for Django Rest Framework
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

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'root.wsgi.application'
AUTH_USER_MODEL = 'users.User'  # Custom user model

DATABASES = {
    'default': {
        'ENGINE': os_environ_get('DATABASE_ENGINE'),
        'NAME': os_environ_get('POSTGRES_DB'),
        'USER': os_environ_get('POSTGRES_USER'),
        'PASSWORD': os_environ_get('POSTGRES_PASSWORD'),
        'HOST': os_environ_get('DATABASE_HOST'),
        'PORT': os_environ_get('DATABASE_PORT'),
    }
}

# Password validation settings
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Rest Framework settings
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

# Swagger settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=45),  # Time for Access Token
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Time for Refresh Token
    'SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD': timedelta(minutes=5),
    # Period after Access Token expires when Refresh Token is still valid (default 5 minutes)
}
