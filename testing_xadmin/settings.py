#-*- coding: UTF-8 -*- 

"""
Django settings for testing_xadmin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')gm9c!49588w$4mfsl8=x$)josvz)%@f2spt^t06y^5jaqqmb9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     ##Ueditor
    'DjangoUeditor',
    'xadmin',
    'crispy_forms',
    # 'reversion',  #  需要pip install django-reversion

    ##For Chuangxing Test
    'chuangxing',
    ##added by Tulpar for  Userena,20140617
    'userena',
    'guardian',  
    'easy_thumbnails',
    'accounts',
    'django_reset',
    ###for img, upload ,resize
    'stdimage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testing_xadmin.urls'

WSGI_APPLICATION = 'testing_xadmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ATOMIC_REQUESTS': True
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'chuangxing_db',
        #'ATOMIC_REQUESTS': True
        'USER' :'tulpar',      # Not used with sqlite3.,
        'PASSWORD' : 'qwe',         # Not used with sqlite3.
        'HOST' : '',           # Set to empty string for localhost. Not used with sqlite3.
        'PORT' : '',            # Set to empty string for default. Not used with sqlite3.
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ZH'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
##added by Tulpar,20140514
import os
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static/ueditor'),
    )

#import os
#settings_dir = os.path.dirname(__file__)
#PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = '/media/'


##added by Tulpar for  Userena,20140617

AUTHENTICATION_BACKENDS = (
        'userena.backends.UserenaAuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

ANONYMOUS_USER_ID = -1


AUTH_PROFILE_MODULE = 'accounts.MyProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'



EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tulpar010@gmail.com'
EMAIL_HOST_PASSWORD = 'TEST818TEST'