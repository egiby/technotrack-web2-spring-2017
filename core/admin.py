from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, FriendshipRequest


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


class ImmutableDatedAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        fields = super(ImmutableDatedAdmin, self).get_readonly_fields(request,
                                                                      obj)

        return list(fields) + ['created']

    # readonly_fields = ('created',)


class DatedAdmin(ImmutableDatedAdmin):
    def get_readonly_fields(self, request, obj=None):
        fields = super(DatedAdmin, self).get_readonly_fields(request,
                                                             obj)

        return list(fields) + ['updated']
    # readonly_fields = ('created', 'updated')


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(DatedAdmin):
    pass


# @admin.register(Friendship)
# class FriendshipAdmin(ImmutableDatedAdmin):
#     pass
