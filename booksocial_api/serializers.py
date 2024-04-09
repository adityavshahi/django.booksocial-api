from rest_framework import serializers


class SayHelloSerializer(serializers.Serializer):
    """Serializes a name field for testing the health of the API ."""
    name = serializers.CharField(max_length=20)


class ViewsetSerializer(serializers.Serializer):
    """Serializes name for using it in the test-viewset"""
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()