from rest_framework import serializers


class RidePricingSerializer(serializers.Serializer):
    distance = serializers.FloatField(min_value=0)
    traffic_level = serializers.ChoiceField(choices=["low", "normal", "high"])
    demand_level = serializers.ChoiceField(choices=["normal", "peak"])
