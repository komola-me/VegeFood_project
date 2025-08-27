from modeltranslation.translator import TranslationOptions
from modeltranslation import translator

from blog.models import BlogCategory, BlogPost, Tag, Comment

@translator.register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)


@translator.register(BlogCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@translator.register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content', )


@translator.register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('text',)