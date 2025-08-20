from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from blog.models import BlogCategory
from blog.serializers import BlogCategoryListSerializer, BlogCategoryCreateUpdateSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryListSerializer
    lookup_field = "id"


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategoryCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"