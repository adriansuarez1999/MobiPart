from .base import *

DEBUG = False

ALLOWED_HOSTS = ['midominio-produccion.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # en caso de usar una postgres
        #'ENGINE': 'django.db.backends.postgresql',

        # En caso de usar una mySQL
        #'ENGINE': 'django.db.backends.mysql',

        # 'NAME': os.getenv('DB_NAME'),
        # 'USER': os.getenv('DB_USER'),
        # 'PASSWORD': os.getenv('DB_PASSWORD'),
        # 'HOST': os.getenv('DB_HOST'),
        # 'PORT': os.getenv('DB_PORT'),       
    }
}

os.environ['DJANGO_PORT'] = '8080'