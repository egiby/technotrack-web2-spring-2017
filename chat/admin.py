from django.contrib import admin

from chat.models import Chat, Message
from core.admin import DatedAdmin


@admin.register(Message)
class MessageAdmin(DatedAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(DatedAdmin):
    pass
