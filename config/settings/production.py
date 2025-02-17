import logging

import sentry_sdk
from django.core.exceptions import DisallowedHost
from sentry_sdk.integrations import logging as sentry_logging
from sentry_sdk.integrations.django import DjangoIntegration

from utils.settings.config import SettingsConfig

from .base import *

EXECUTION_ENVIRONMENT = env.str(
    "DJANGO_EXECUTION_ENVIRONMENT",
    default=SettingsConfig.ExecutionEnvironment.PRODUCTION,
)

# Logging
SENTRY_DSN = env.str("DJANGO_SENTRY_DSN", default=None)
# ________________LOGGING_____________________
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
        ],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        environment="RideHailingApp",
        debug=False,
        ignore_errors=[DisallowedHost],
        profiles_sample_rate=1.0,
    )
    sentry_logging.ignore_logger("django.security.DisallowedHost")
else:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s :: %(name)s - %(levelname)s - %(message)s",
    )
