from django.db.models.signals import post_save

from core.models import Friendship, FriendshipRequest


def check_friendship(instance, created=False, *args, **kwargs):
    if instance.is_confirmed and \
            not len(Friendship.objects.filter(first=instance.author)):
        friendship = Friendship()
        friendship.first = instance.author
        friendship.second = instance.user
        friendship.save()


def add_pair(instance, created=False, *args, **kwargs):
    if created and not len(Friendship.objects.filter(second=instance.first,
                                                     first=instance.second)):
        friendship = Friendship()
        friendship.first = instance.second
        friendship.second = instance.first
        friendship.save()

post_save.connect(check_friendship, sender=FriendshipRequest)
post_save.connect(add_pair, sender=Friendship)
