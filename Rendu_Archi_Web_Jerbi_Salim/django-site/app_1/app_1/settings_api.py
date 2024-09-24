from .settings import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Spécifique à l'API
    'api',  # App de l'API
]

ROOT_URLCONF = 'app_1.urls_api'
WSGI_APPLICATION = 'app_1.wsgi.application'
