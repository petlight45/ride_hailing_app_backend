from django.conf import settings
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class RidePricingAPITest(TestCase):
    def setUp(self):
        """Initialize test client"""
        self.client = APIClient()
        self.headers = {"api-key": settings.GUEST_ENDPOINT_API_KEY}

    def _make_call(self, params):
        return self.client.get("/api/calculate_fare/", params, **self.headers)

    def test_standard_fare_calculation(self):
        """Test API response for standard fare"""
        response = self._make_call(
            {"distance": 5, "traffic_level": "low", "demand_level": "normal"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_fare"], 7.5)  # 2.5 + (5 * 1.0)

    def test_high_traffic_pricing(self):
        """Test API response for high traffic pricing"""
        response = self._make_call(
            {"distance": 8, "traffic_level": "high", "demand_level": "normal"}
        )
        expected_fare = round((2.5 + (8 * 1.0)) * 1.5, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_fare"], expected_fare)

    def test_surge_pricing_high_demand(self):
        """Test API response for demand surge pricing"""
        response = self._make_call(
            {"distance": 12, "traffic_level": "normal", "demand_level": "peak"}
        )
        expected_fare = round((2.5 + (12 * 1.0)) * 1.2 * 1.8, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_fare"], expected_fare)

    def test_peak_hour_with_high_traffic(self):
        """Test API response for peak hour + high traffic pricing"""
        response = self._make_call(
            {"distance": 7, "traffic_level": "high", "demand_level": "peak"}
        )
        expected_fare = round((2.5 + (7 * 1.0)) * 1.5 * 1.8, 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_fare"], expected_fare)

    def test_long_distance_ride(self):
        """Test API response for long-distance ride"""
        response = self._make_call(
            {"distance": 20, "traffic_level": "low", "demand_level": "normal"}
        )
        expected_fare = round(2.5 + (20 * 1.0), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_fare"], expected_fare)

    def test_invalid_request(self):
        """Test API response for invalid input (negative distance)"""
        response = self._make_call(
            {"distance": -5, "traffic_level": "low", "demand_level": "normal"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
