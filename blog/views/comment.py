from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from blog.models import Comment
from blog.serializers import CommentCreateSerializer, CommentListSerializer


class PostCommentListAPIView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("user",)
    lookup_field = "post_id"

    def get_queryset(self):
        return Comment.objects.filter(is_active=True, post=self.kwargs["post_id"])


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.filter(is_active=True)
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Comment.objects.filter(is_active=True, user=self.request.user)