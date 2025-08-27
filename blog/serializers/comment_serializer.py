from rest_framework import serializers

from blog.choices import BlogPostStatus
from blog.models import BlogPost, Comment
from users.models import User


class CommentUserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "avatar",
        ]


class CommentPostNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
        ]


class CommentListSerializer(serializers.ModelSerializer):
    user = CommentUserNestedSerializer()
    post = CommentPostNestedSerializer()

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "user",
            "text",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=BlogPost.objects.all()
    )

    class Meta:
        model = Comment
        fields = ["id", "post", "text", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "is_active", "created_at", "updated_at"]

    def save(self, **kwargs):
        print(kwargs, self)
        post = self.validated_data.get("post")

        if post.status == BlogPostStatus.DRAFT:
            raise serializers.ValidationError("You can't comment on a draft post.")

        return super().save(**kwargs)