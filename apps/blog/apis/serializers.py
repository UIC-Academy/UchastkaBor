from rest_framework import serializers

from apps.blog.models import Post


# class BlogPostListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(read_only=True)
#     slug = serializers.CharField(read_only=True, required=False)
#     subtitle = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "slug", "created_at"]