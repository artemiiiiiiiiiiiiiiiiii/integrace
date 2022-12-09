from rest_framework import serializers


class ReplaceSerializer(serializers.Serializer):
    text = serializers.CharField()
    result = serializers.CharField()
