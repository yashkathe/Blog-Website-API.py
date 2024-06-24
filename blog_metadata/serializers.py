from rest_framework import serializers
from .models import Blog


class BlogMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "description",
            "tags",
            "content",
            "route",
            "date",
        ]

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "route",
        ]

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
        ]
