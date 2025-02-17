from django.test import TestCase

from app.api.public.services.pricing import RidePricingService


class RidePricingServiceTest(TestCase):
    def test_standard_fare_calculation(self):
        """Test base fare + distance fare with no multipliers"""
        fare = RidePricingService.get_fare(
            distance_km=5, traffic_level="low", demand_level="normal"
        )
        expected_total = round(2.5 + (5 * 1.0), 2)  # Base fare + per km rate
        self.assertEqual(fare["total_fare"], expected_total)

    def test_high_traffic_pricing(self):
        """Test fare calculation with high traffic multiplier (1.5x)"""
        fare = RidePricingService.get_fare(
            distance_km=8, traffic_level="high", demand_level="normal"
        )
        expected_total = round((2.5 + (8 * 1.0)) * 1.5, 2)  # Apply traffic multiplier
        self.assertEqual(fare["total_fare"], expected_total)

    def test_surge_pricing_high_demand(self):
        """Test fare calculation with demand surge multiplier (1.8x)"""
        fare = RidePricingService.get_fare(
            distance_km=12, traffic_level="normal", demand_level="peak"
        )
        expected_total = round(
            (2.5 + (12 * 1.0)) * 1.2 * 1.8, 2
        )  # Apply demand surge multiplier
        self.assertEqual(fare["total_fare"], expected_total)

    def test_peak_hour_with_high_traffic(self):
        """Test fare calculation with both traffic and demand multipliers"""
        fare = RidePricingService.get_fare(
            distance_km=7, traffic_level="high", demand_level="peak"
        )
        expected_total = round(
            (2.5 + (7 * 1.0)) * 1.5 * 1.8, 2
        )  # Apply both multipliers
        self.assertEqual(fare["total_fare"], expected_total)

    def test_long_distance_ride(self):
        """Test fare calculation for a long distance ride"""
        fare = RidePricingService.get_fare(
            distance_km=20, traffic_level="low", demand_level="normal"
        )
        expected_total = round(2.5 + (20 * 1.0), 2)  # No multipliers
        self.assertEqual(fare["total_fare"], expected_total)
