from rest_framework import generics
from rest_framework import permissions

from blog.serializers import PostSerializer
from blog.models import BlogPost

class PostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostDetailsAPIView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"


class PostCreateAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "id"


class FeaturedPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return super().get_queryset().filter(is_featured=True)[:5]
