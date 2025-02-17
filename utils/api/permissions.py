from django.conf import settings
from rest_framework.permissions import BasePermission


class GuestEndpoint:
    class IsAuthorizedForGuestEndpoint(BasePermission):
        _AUTH_CONTEXT_FIELD_NAME = "api-key"

        def get_auth_context(self, request):
            return request.META.get(
                f"HTTP_{self._AUTH_CONTEXT_FIELD_NAME.replace('-', '_').upper()}"
            ) or request.META.get(self._AUTH_CONTEXT_FIELD_NAME)

        def has_permission(self, request, view):
            auth_context = self.get_auth_context(request)
            return auth_context and auth_context == settings.GUEST_ENDPOINT_API_KEY
