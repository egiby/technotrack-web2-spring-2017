from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Authored(models.Model):
    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class UnchangeableDated(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Dated(UnchangeableDated):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Named(models.Model):
    name = models.CharField(max_length=127)

    class Meta:
        abstract = True


class FriendshipRequest(Authored, Dated):
    is_confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='recipient')


class Friendship(UnchangeableDated):
    first = models.ForeignKey(User, related_name='first')
    second = models.ForeignKey(User, related_name='second')
