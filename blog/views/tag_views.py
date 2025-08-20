from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from blog.serializers import TagListSerializer, TagCreateUpdateSerializer
from blog.models import Tag


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TagDetailAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    lookup_field = "id"


class TagCreateAPIView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class TagUpdateAPIView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"


class TagDeleteAPIView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagCreateUpdateSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "id"
