from rest_framework import decorators, response, status, viewsets

from app.api.public.controllers.pricing import RidePricingController
from app.api.public.serializers import RidePricingSerializer
from utils.api.permissions import GuestEndpoint
from utils.mixins import ViewSetMixin


class RidePricingViewSet(
    ViewSetMixin.Validator.CustomRequestDataValidationMixin, viewsets.ViewSet
):
    permission_classes = [GuestEndpoint.IsAuthorizedForGuestEndpoint]

    def get_required_fields(self):
        if self.action == "calculate_fare":
            return ["distance", "traffic_level", "demand_level"]

    @decorators.action(detail=False, methods=["get"])
    def calculate_fare(self, request, *args, **kwargs):
        serializer = RidePricingSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        fare_details = RidePricingController.calculate_fare(
            distance=serializer.validated_data["distance"],
            traffic_level=serializer.validated_data["traffic_level"],
            demand_level=serializer.validated_data["demand_level"],
        )
        return response.Response(fare_details, status=status.HTTP_200_OK)
