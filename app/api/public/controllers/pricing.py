from app.api.public.services.pricing import RidePricingService


class RidePricingController:
    @staticmethod
    def calculate_fare(distance, traffic_level, demand_level):
        return RidePricingService.get_fare(
            distance_km=distance, traffic_level=traffic_level, demand_level=demand_level
        )
