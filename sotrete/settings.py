"""
Configuration Django pour le projet sotrete.

Généré par 'django-admin startproject' avec Django.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/stable/topics/settings/

Pour la liste complète des paramètres et leurs valeurs, voir
https://docs.djangoproject.com/en/stable/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
import dj_database_url

# Construction des chemins dans le projet comme ceci : BASE_DIR / 'sous-dossier'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Paramètres de démarrage rapide - inadaptés à la production
# Voir https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['*']

# Définition des applications
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # Whitenoise pour servir les fichiers statiques en développement
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sotreteapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise pour servir les fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Activer la compression et le cache des fichiers statiques
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'sotrete.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sotrete.wsgi.application'

# Base de données
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}

# Validation des mots de passe
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalisation
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichiers statiques (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'staticfiles'))

# Fichiers média (Images, Téléchargements)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Type de champ de clé primaire par défaut
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration de l'email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mranebaye@gmail.com'
EMAIL_HOST_PASSWORD = 'itpd-xqcl-mpzm-dvtw'
EMAIL_USE_TLS = True