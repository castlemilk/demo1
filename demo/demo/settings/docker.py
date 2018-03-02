from demo.settings.base import *  # NOQA (ignore all errors on this line)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "app", "images"),

]
DEBUG = True # disabling debug mode will cause staticfiles to not be cheaply served by django :(
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'demo',
        'USER': 'demo',
        'PASSWORD': 'password',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}