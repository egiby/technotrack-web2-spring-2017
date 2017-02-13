from django.db import models
from django.conf import settings


from core.models import Authored, Dated, Named


class Chat(Authored, Dated, Named):
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')

    class Meta:
        pass

    def __str__(self):
        return self.name


class Message(Authored, Dated):
    chat = models.ForeignKey(Chat)
    text = models.TextField()

    def __str__(self):
        return str(self.updated)
