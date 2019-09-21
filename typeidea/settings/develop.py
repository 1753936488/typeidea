from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'mathartsys',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
