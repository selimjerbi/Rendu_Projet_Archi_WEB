from .settings import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'public',  # App spécifique à Public
]

ROOT_URLCONF = 'app_1.urls_public'
WSGI_APPLICATION = 'app_1.wsgi.application'
