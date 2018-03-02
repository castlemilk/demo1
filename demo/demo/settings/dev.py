from demo.settings.base import *  # NOQA (ignore all errors on this line)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app',
        'USER': 'castlemilk',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}