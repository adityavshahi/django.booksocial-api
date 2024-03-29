from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    """Serializes a name field for testing the health of the API ."""
    name = serializers.CharField(max_length=20)