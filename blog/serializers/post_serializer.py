from rest_framework import serializers

from blog.models import BlogPost
from . import TagListSerializer, BlogCategoryListSerializer, AuthorSerializer

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = BlogCategoryListSerializer(read_only=True)
    tags = TagListSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'image', 'status', 'is_featured', 'published_at', 'author', 'category', 'tags']
