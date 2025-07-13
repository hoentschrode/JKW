from .base import *  # noqa: F403

DEBUG = True

SECRET_KEY = "django-insecure-zd_cpg&6f)rfybd91i34!w^ebf-t%vd%oll)vw^4(vey^bfu7y"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *  # noqa
except ImportError:
    pass
