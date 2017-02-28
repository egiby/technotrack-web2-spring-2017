from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', null=True)


class Authored(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True


class ImmutableDated(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Dated(ImmutableDated):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Named(models.Model):
    name = models.CharField(max_length=127)

    class Meta:
        abstract = True


class FriendshipRequest(Authored, Dated):
    is_confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recipient')


class Friendship(ImmutableDated):
    first = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='friends')
    second = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='second')

    def __str__(self):
        return str(self.first) + ' ' + str(self.second)


def get_friends(user):
    friendships = Friendship.objects.filter(first=user)
    return map(lambda pair: pair.second, friendships)
