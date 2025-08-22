from modeltranslation.translator import TranslationOptions
from modeltranslation import translator

from blog.models import BlogCategory, BlogPost, Tag, Comment

@translator.register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)


@translator.register(BlogCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'is_active')


@translator.register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content', 'image','status', 'is_featured', 'published_at', 'author', 'category', 'tags',)


@translator.register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('post', 'user', 'text', 'is_active')