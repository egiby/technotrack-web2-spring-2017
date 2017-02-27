from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin

from core.admin import ImmutableDatedAdmin
from .models import Like


class LikeInline(admin.TabularInline, GenericInlineModelAdmin):
    model = Like

    ct_field = 'target_content_type'
    ct_fk_field = 'target_id'

    readonly_fields = 'created',
    extra = 0


class LikeAbleAdmin(admin.ModelAdmin):
    inlines = LikeInline,


@admin.register(Like)
class LikeAdmin(ImmutableDatedAdmin):
    pass
