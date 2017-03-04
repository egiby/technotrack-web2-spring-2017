from django.db.models.signals import post_save, post_delete

from core.models import get_friends
from .models import Post


def garbage_collector(sender, instance, *args, **kwargs):
    if Post.objects.filter(content_id=instance.content_id):
        return

    instance.content.delete()


post_delete.connect(garbage_collector, sender=Post)
