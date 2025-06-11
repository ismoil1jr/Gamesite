"""
Django settings for game project.
"""

from pathlib import Path
import os

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-7@y)*bmgfnw@y@ls3-n*_(us8%@@jdb))6zyn4pk-^w3up*b=j'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Temporary for development, specify exact hosts in production

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'parler',
    'django_ckeditor_5',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Moved up for proper language detection
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'game.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # Added for translation
            ],
        },
    },
]

WSGI_APPLICATION = 'game.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Русский'),
    ('uz', 'Oʻzbekcha'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'},
        {'code': 'ru'},
        {'code': 'uz'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}

# Static & Media files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'  # Fixed typo (was MEIDA_URL)
MEDIA_ROOT = BASE_DIR / 'media'

# CKEditor 5 Configuration (single consolidated config)
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 
            'bold', 'italic', 'link', 'underline', 'strikethrough',
            '|', 'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'
        ],
        'language': 'en',
    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|', 'bulletedList', 'numberedList', '|', 'blockQuote',
        ],
        'toolbar': [
            'heading', '|', 'outdent', 'indent', '|',
            'bold', 'italic', 'link', 'underline', 'strikethrough', 'code',
            'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing',
            'insertImage', 'bulletedList', 'numberedList', 'todoList', '|',
            'blockQuote', 'imageUpload', '|', 'fontSize', 'fontFamily',
            'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
            'insertTable',
        ],
        'image': {
            'toolbar': [
                'imageTextAlternative', '|',
                'imageStyle:alignLeft', 'imageStyle:alignRight',
                'imageStyle:alignCenter', 'imageStyle:side', '|'
            ],
            'styles': [
                'full', 'side', 'alignLeft', 'alignRight', 'alignCenter'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells',
                'tableProperties', 'tableCellProperties'
            ]
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        }
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'