from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from utils.helpers.commons.utils.secrets import Secrets
from utils.settings.config import SettingsConfig

urlpatterns = [
    path(
        f"{Secrets.generate_random_token(10) if settings.EXECUTION_ENVIRONMENT == SettingsConfig.ExecutionEnvironment.PRODUCTION else 'admin'}/",
        admin.site.urls,
    ),
    path("api/", include("app.api.public.urls.guest"), name="api_public_guest"),
]
