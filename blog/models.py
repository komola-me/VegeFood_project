from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.choices import BlogPostStatus
from common.models import BaseModel

User = get_user_model()


class BlogPost(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Post Title"))
    slug = models.SlugField(unique_for_date="published_at", verbose_name=_("slug"))
    content = models.TextField(verbose_name=_("content"))
    image = models.ImageField(upload_to="blog/", blank=True, null=True, verbose_name=_("image"))
    status = models.CharField(
        max_length=10, choices=BlogPostStatus.choices, default=BlogPostStatus.DRAFT, verbose_name=_("status")
    )
    is_featured = models.BooleanField(default=False, verbose_name=_("is_featured"))
    published_at = models.DateTimeField(blank=True, null=True, verbose_name=_("Published at"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name=_("Author"))
    category = models.ForeignKey(
        "blog.BlogCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name=_("Post Category")
    )
    tags = models.ManyToManyField("blog.Tag", blank=True, related_name="posts", verbose_name=_("Post Tags"))

    class Meta:
        ordering = ["-published_at"]
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")

    def __str__(self):
        return self.title


class BlogCategory(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Blog Category"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Tag Name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Comment(BaseModel):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments", verbose_name=_("post")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name=_("Comment Author"))
    text = models.TextField(verbose_name=_("Comment text"))
    is_active = models.BooleanField(default=True, verbose_name=_("Comment Is Active"))

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")