class RidePricingModel:
    BASE_FARE = 2.5
    PER_KM_RATE = 1.0

    @classmethod
    def calculate_fare(cls, distance_km, traffic_multiplier=1.0, demand_multiplier=1.0):
        distance_fare = cls.PER_KM_RATE * distance_km
        total_fare = (
            (cls.BASE_FARE + distance_fare) * traffic_multiplier * demand_multiplier
        )
        return {
            "base_fare": cls.BASE_FARE,
            "distance_fare": distance_fare,
            "traffic_multiplier": traffic_multiplier,
            "demand_multiplier": demand_multiplier,
            "total_fare": round(total_fare, 2),
        }
