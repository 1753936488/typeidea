from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'USER': 'root',
        'PASSWORD': 'mathartsys',
        'HOST': 'godyao.club',
        'PORT': 3306,
    }
}

