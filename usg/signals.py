from django.db.models.signals import post_save

from core.models import get_friends
from .models import Post, Event


def create_feed_events(instance, created=False, *args, **kwargs):
    if not created:
        return

    for friend in list(get_friends(instance.author)) + [instance.author]:
        event = Event()
        event.user = friend
        event.post = instance
        event.save()


post_save.connect(create_feed_events, sender=Post)
