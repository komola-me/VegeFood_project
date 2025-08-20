from category_views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,
)
from tag_views import (
    TagListAPIView,
    TagDetailAPIView,
    TagCreateAPIView,
    TagUpdateAPIView,
    TagDeleteAPIView
)
from post_views import (
    PostListAPIView,
    PostDetailsAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    FeaturedPostListAPIView,
)

__all__ = [
    "CategoryListAPIView",
    "CategoryDetailAPIView",
    "CategoryCreateAPIView",
    "CategoryUpdateAPIView",
    "CategoryDeleteAPIView",

    "TagListAPIView",
    "TagDetailAPIView",
    "TagCreateAPIView",
    "TagUpdateAPIView",
    "TagDeleteAPIView",

    "PostListAPIView",
    "PostDetailsAPIView",
    "PostCreateAPIView",
    "PostUpdateAPIView",
    "PostDeleteAPIView",
    "FeaturedPostListAPIView",
]