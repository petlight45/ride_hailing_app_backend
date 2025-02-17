import logging

from utils.settings.config import SettingsConfig

from .base import *

EXECUTION_ENVIRONMENT = env.str(
    "DJANGO_EXECUTION_ENVIRONMENT", default=SettingsConfig.ExecutionEnvironment.LOCAL
)

# ________________LOGGING_____________________
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s :: %(name)s - %(levelname)s - %(message)s"
)
