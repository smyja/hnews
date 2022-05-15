from rest_framework import serializers
from news.models import Stories


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        read_only_fields = [
            "synced",
            "kids",
            "descendants",
            "score",
            "slug",
        ]
        fields = (
            "story_id",
            "title",
            "story_type",
            "author",
            "url",
            "kids",
            "time",
            "descendants",
            "score",
            "text",
            "dead",
            "slug",
        )
