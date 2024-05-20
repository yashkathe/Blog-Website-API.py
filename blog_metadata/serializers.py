from rest_framework import serializers
from .models import BlogMetaData


class BlogMetaData(serializers.ModelSerializer):
    class Meta:
        model = BlogMetaData
        fields = [
            "id",
            "title",
            "description",
            "tags",
            "route",
            "componentName",
            "date"
        ]
