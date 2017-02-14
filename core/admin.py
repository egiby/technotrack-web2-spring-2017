from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, FriendshipRequest


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


class ImmutableDatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


class DatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(DatedAdmin):
    pass


# @admin.register(Friendship)
# class FriendshipAdmin(ImmutableDatedAdmin):
#     pass
