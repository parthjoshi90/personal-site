# flake8: noqa

from .base import *
from decouple import Csv, config

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SESSION_COOKIE_SECURE = True


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================


# ==============================================================================
# THIRD-PARTY APPS
# ==============================================================================

# ==============================================================================
# STATIC
# ==============================================================================
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ==============================================================================
# django-compressor
# ==============================================================================

# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
COMPRESS_ENABLED = config("COMPRESS_ENABLED", default=True, cast=bool)
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_URL
COMPRESS_URL = STATIC_URL  # noqa F405
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True  # Offline compression is required when using Whitenoise
# https://django-compressor.readthedocs.io/en/latest/settings/#django.conf.settings.COMPRESS_FILTERS
COMPRESS_FILTERS = {
    "css": [
        "compressor.filters.css_default.CssAbsoluteFilter",
        "compressor.filters.cssmin.rCSSMinFilter",
    ],
    "js": ["compressor.filters.jsmin.JSMinFilter"],
}