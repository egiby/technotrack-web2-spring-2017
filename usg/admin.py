from django.contrib import admin

from core.admin import DatedAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(DatedAdmin):
    pass

