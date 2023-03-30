"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e8so$%@^-6^_&^tuv$%26z2zw(c6*3)w0mss4pzx3hx9_)!&5u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    #'material',
    #'material.admin', 
    #'material.admin.default',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplicaciones.blog',
    'import_export',
    'ckeditor',
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

ROOT_URLCONF = 'django_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database

# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD': 'OhqIu72aSqdwYeC1v5RM',
        'HOST': 'containers-us-west-162.railway.app',
        'PORT': 6287,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


#Agrega una paleta mas completa para CKEDITOR
CKEDITOR_CONFIGS = {

      'default': {
         'toolbar':'full',
    },
}


LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MATERIAL_ADMIN_SITE = {
   # 'HEADER': 'Mi primier sitio',  # Admin site header
    #'TITLE':  'Mi Blog',  # Admin site title
   # 'FAVICON':'path/to/favicon',  # Admin site favicon (path to static should be specified)
   # 'MAIN_BG_COLOR': 'green',  # Admin site main color, css color should be specified
    #'MAIN_HOVER_COLOR':'red',  # Admin site main hover color, css color should be specified
  #  'PROFILE_PICTURE':'path/to/image',  # Admin site profile picture (path to static should be specified)
   #'PROFILE_BG':'path/to/image',  # Admin site profile background (path to static should be specified)
   # 'LOGIN_LOGO':'path/to/image',  # Admin site logo on login page (path to static should be specified)
   # 'LOGOUT_BG':'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES': True,  #  Show default admin themes button
    'TRAY_REVERSE':False,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE':True,  # Hide side navbar by default
    'SHOW_COUNTS':True, # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
        'sites': 'send',
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
}

