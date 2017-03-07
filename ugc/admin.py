from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from core.admin import DatedAdmin
from likes.admin import LikeAbleAdmin
from .models import Post, TextContent


class PostInline(admin.TabularInline, GenericInlineModelAdmin):
    model = Post

    ct_field = 'content_type'
    ct_fk_field = 'content_id'

    extra = 0
    readonly_fields = 'author', 'name'


@admin.register(Post)
class PostAdmin(DatedAdmin, LikeAbleAdmin):
    pass


@admin.register(TextContent)
class TextContentAdmin(admin.ModelAdmin):
    inlines = PostInline,

