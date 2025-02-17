from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter


class RouterUtils:
    @staticmethod
    def get_router():
        if settings.DEBUG:
            return DefaultRouter()
        else:
            return SimpleRouter()
