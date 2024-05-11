"""
Django settings for blog_demo1 project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
########################### 开发自定义内容 #########################
print("当前project的baseDir=", BASE_DIR)
########################### 开发自定义内容 #########################

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d1)rm8#ay-hwkz_))(6=$4_5d%7u=v(333yeimw#+4s3*j4)p5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    ########################### 开发自定义内容 #########################
    # 业务模块，用业务模块来分隔的。有新的业务模块后，才加入
    ########################### 开发自定义内容 #########################
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blog_demo1.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        ########################### 开发自定义内容 #########################
        # 需要给DIRS属性添加新的内容
        ########################### 开发自定义内容 #########################
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blog_demo1.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    ########################### 开发自定义内容 #########################
    # 数据库的配置信息，想更换成其他数据库时可以修改，配置项有下面这些
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': '127.0.0.1',
    #     'PORT': 3306,
    #     'USER': 'root',
    #     'PASSWORD': '123456',
    #     'NAME': 'python_blog',
    # }
    ########################### 开发自定义内容 #########################
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

########################### 开发自定义内容 #########################
# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# 修改语言显示
LANGUAGE_CODE = "zh-Hans"

# 修改时区
TIME_ZONE = "Asia/Shanghai"
########################### 开发自定义内容 #########################


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

########################### 开发自定义内容 #########################
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
########################### 开发自定义内容 #########################

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"