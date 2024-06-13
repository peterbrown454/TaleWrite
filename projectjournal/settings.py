from pathlib import Path
import os
import dj_database_url
if os.path.isfile("env.py"):
    import env


BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY =  os.environ.get('SECRET_KEY')


DEBUG = False
ALLOWED_HOSTS = ['8000-peterbrown454-talewrite-p8b55v737kg.ws-eu114.gitpod.io', '8000-peterbrown454-diary-ewoyturoyqk.ws-eu111.gitpod.io', 'talewrite-b9287c77cba0.herokuapp.com', 'journap-15c9108ba52d.herokuapp.com', 'journap-c86fda53e915.herokuapp.com', '8000-peterbrown454-diary-b6qovr99y0h.ws-eu110.gitpod.io', 'gitpod.io', 'herokuapp.com', '8000-peterbrown454-diary-ewoyturoyqk.ws-eu110.gitpod.io']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'journapp',
    'projectjournal',
    'entries',
    'accounts',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projectjournal.urls'

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

WSGI_APPLICATION = 'projectjournal.wsgi.application'

DATABASES = {
'default':
dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeanyapp.com",
    "https://*.herokuapp.com",
    "https://*.gitpod.io",
]



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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE ='cloudinary_storage.storage.MediaCloudinaryStorage'




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

