from app.api.public.domain.pricing import RidePricingModel


class RidePricingService:
    TRAFFIC_MULTIPLIERS = {"low": 1.0, "normal": 1.2, "high": 1.5}

    DEMAND_MULTIPLIERS = {"normal": 1.0, "peak": 1.8}

    @classmethod
    def get_fare(cls, distance_km, traffic_level, demand_level):
        # Get multipliers
        traffic_multiplier = cls.TRAFFIC_MULTIPLIERS.get(traffic_level, 1.0)
        demand_multiplier = cls.DEMAND_MULTIPLIERS.get(demand_level, 1.0)

        # Calculate final fare
        return RidePricingModel.calculate_fare(
            distance_km, traffic_multiplier, demand_multiplier
        )
