from rest_framework import serializers
from .models import BlogMetaData


class BlogMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMetaData
        fields = [
            "id",
            "title",
            "description",
            "tags",
            "route",
            "componentName",
            "date",
        ]

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogMetaData
        fields = [
            "id",
            "route",
            "componentName"
        ]