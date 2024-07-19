import os
import random
import string

from .base import *

DEBUG = False

if "DJANGO_SECRET_KEY" in os.environ:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
else:

    print(
        "WARNING: DJANGO_SECRET_KEY not found in os.environ. Generating ephemeral SECRET_KEY."
    )
    SECRET_KEY = "".join(
        [random.SystemRandom().choice(string.printable) for i in range(50)]
    )

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if "PRIMARY_HOST" in os.environ:
    WAGTAILADMIN_BASE_URL = "https://{}".format(os.environ["PRIMARY_HOST"])


# AWS creds may be used for S3 and/or Elasticsearch
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_REGION = os.getenv("AWS_REGION", "")

REDIS_URL = os.environ.get("REDIS_TLS_URL", os.environ.get("REDIS_URL"))
if REDIS_URL:
    connection_pool_kwargs = {}

    if REDIS_URL.startswith("rediss"):
        # Heroku Redis uses self-signed certificates for secure redis connections
        # When using TLS, we need to disable certificate validation checks.
        connection_pool_kwargs["ssl_cert_reqs"] = None

    redis_options = {
        "IGNORE_EXCEPTIONS": True,
        "SOCKET_CONNECT_TIMEOUT": 2,  # seconds
        "SOCKET_TIMEOUT": 2,  # seconds
        "CONNECTION_POOL_KWARGS": connection_pool_kwargs,
    }

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL + "/0",
            "OPTIONS": redis_options,
        },
        "renditions": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL + "/1",
            "OPTIONS": redis_options,
        },
    }
    DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "bakerydemo",
        }
    }

ELASTICSEARCH_ENDPOINT = os.getenv("ELASTICSEARCH_ENDPOINT", "")

if ELASTICSEARCH_ENDPOINT:
    from elasticsearch import RequestsHttpConnection

    WAGTAILSEARCH_BACKENDS = {
        "default": {
            "BACKEND": "wagtail.search.backends.elasticsearch5",
            "HOSTS": [
                {
                    "host": ELASTICSEARCH_ENDPOINT,
                    "port": int(os.getenv("ELASTICSEARCH_PORT", "9200")),
                    "use_ssl": os.getenv("ELASTICSEARCH_USE_SSL", "off") == "on",
                    "verify_certs": os.getenv("ELASTICSEARCH_VERIFY_CERTS", "off")
                    == "on",
                }
            ],
            "OPTIONS": {
                "connection_class": RequestsHttpConnection,
            },
        }
    }

    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        from aws_requests_auth.aws_auth import AWSRequestsAuth

        WAGTAILSEARCH_BACKENDS["default"]["HOSTS"][0]["http_auth"] = AWSRequestsAuth(
            aws_access_key=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_token=os.getenv("AWS_SESSION_TOKEN", ""),
            aws_host=ELASTICSEARCH_ENDPOINT,
            aws_region=AWS_REGION,
            aws_service="es",
        )
    elif AWS_REGION:
        # No API keys in the environ, so attempt to discover them with Boto instead, per:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials
        # This may be useful if your credentials are obtained via EC2 instance meta data.
        from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

        WAGTAILSEARCH_BACKENDS["default"]["HOSTS"][0]["http_auth"] = (
            BotoAWSRequestsAuth(
                aws_host=ELASTICSEARCH_ENDPOINT,
                aws_region=AWS_REGION,
                aws_service="es",
            )
        )

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if "AWS_STORAGE_BUCKET_NAME" in os.environ:
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_QUERYSTRING_AUTH = False
    INSTALLED_APPS.append("storages")
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = "private"
    if "AWS_S3_CUSTOM_DOMAIN" in os.environ:
        AWS_S3_CUSTOM_DOMAIN = os.environ["AWS_S3_CUSTOM_DOMAIN"]
    if "AWS_S3_REGION_NAME" in os.environ:
        AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]

if "GS_BUCKET_NAME" in os.environ:
    GS_BUCKET_NAME = os.getenv("GS_BUCKET_NAME")
    GS_PROJECT_ID = os.getenv("GS_PROJECT_ID")
    GS_DEFAULT_ACL = "publicRead"
    GS_AUTO_CREATE_BUCKET = True

    INSTALLED_APPS.append("storages")
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
}

# Front-end cache
if (
    "FRONTEND_CACHE_CLOUDFLARE_TOKEN" in os.environ
    or "FRONTEND_CACHE_CLOUDFLARE_BEARER_TOKEN" in os.environ
):
    INSTALLED_APPS.append("wagtail.contrib.frontend_cache")
    WAGTAILFRONTENDCACHE = {
        "default": {
            "BACKEND": "wagtail.contrib.frontend_cache.backends.CloudflareBackend",
            "ZONEID": os.environ["FRONTEND_CACHE_CLOUDFLARE_ZONEID"],
        }
    }

    if "FRONTEND_CACHE_CLOUDFLARE_TOKEN" in os.environ:
        # To use an account-wide API key, set the following:
        #  * $FRONTEND_CACHE_CLOUDFLARE_TOKEN
        #  * $FRONTEND_CACHE_CLOUDFLARE_EMAIL
        #  * $FRONTEND_CACHE_CLOUDFLARE_ZONEID
        # These can be obtained from a sysadmin.
        WAGTAILFRONTENDCACHE["default"].update(
            {
                "EMAIL": os.environ["FRONTEND_CACHE_CLOUDFLARE_EMAIL"],
                "TOKEN": os.environ["FRONTEND_CACHE_CLOUDFLARE_TOKEN"],
            }
        )

    else:
        # To use an API token with restricted access, set the following:
        #  * $FRONTEND_CACHE_CLOUDFLARE_BEARER_TOKEN
        #  * $FRONTEND_CACHE_CLOUDFLARE_ZONEID
        WAGTAILFRONTENDCACHE["default"].update(
            {"BEARER_TOKEN": os.environ["FRONTEND_CACHE_CLOUDFLARE_BEARER_TOKEN"]}
        )
# Basic authentication settings
# These are settings to configure the third-party library:
if os.environ.get("BASIC_AUTH_ENABLED", "false").lower().strip() == "true":
    # Insert basic auth as a first middleware to be checked first, before
    # anything else.
    MIDDLEWARE.insert(0, "baipw.middleware.BasicAuthIPWhitelistMiddleware")

    # This is the credentials users will have to use to access the site.
    BASIC_AUTH_LOGIN = os.environ.get("BASIC_AUTH_LOGIN", "villarosauser")
    BASIC_AUTH_PASSWORD = os.environ.get("BASIC_AUTH_PASSWORD", "villarosapass")

    # Wagtail requires Authorization header to be present for the previews
    BASIC_AUTH_DISABLE_CONSUMING_AUTHORIZATION_HEADER = True

    # This is the list of hosts that website can be accessed without basic auth
    # check.
    if "BASIC_AUTH_WHITELISTED_HTTP_HOSTS" in os.environ:
        BASIC_AUTH_WHITELISTED_HTTP_HOSTS = os.environ[
            "BASIC_AUTH_WHITELISTED_HTTP_HOSTS"
        ].split(",")

    BASIC_AUTH_RESPONSE_TEMPLATE = "base/basic_auth.html"

# Force HTTPS redirect (enabled by default!)
SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEFAULT_HSTS_SECONDS = 30 * 24 * 60 * 60  # 30 days
SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", DEFAULT_HSTS_SECONDS))
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_CONTENT_TYPE_NOSNIFF = True

# Referrer-policy header settings.
REFERRER_POLICY = os.environ.get(  # noqa
    "SECURE_REFERRER_POLICY", "no-referrer-when-downgrade"
).strip()


try:
    from .local import *
except ImportError:
    pass
