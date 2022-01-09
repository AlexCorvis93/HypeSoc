from .base import *

ENVIRONMENT = 'development'

DEBUG = True

SECRET_KEY = 'django-insecure-d2xithk#4j*mu^8ehi%6!lolwwmoe0(72dk*5b95#f*=c+6z1!'

DB_CONFIG = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hype',
        'USER': 'admin',
        'PASSWORD': 'popa123',
        'HOST': 'localhost',
        'PORT': '',
    }


DATABASES = {
    'default': DB_CONFIG
}