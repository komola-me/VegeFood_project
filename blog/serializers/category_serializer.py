from rest_framework import serializers

from blog.models import BlogCategory

class BlogCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["id", "name", "is_active"]
        read_only_fields = ["id", "created_at", "updated_at"]


class BlogCategoryCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ["name", "is_active"]