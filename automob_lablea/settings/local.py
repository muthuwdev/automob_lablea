from .base import *  # noqa
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="PR4AI6GzsM98FyyCErCWzPEIS2puPJ3zbSH1vjirStvC529E-WE",
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
# EMAIL_PORT = env("EMAIL_PORT")
# DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
# DOMAIN = env("DOMAIN")
# SITE_NAME = "Authors Haven"
