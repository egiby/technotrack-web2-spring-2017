from django.db.models.signals import post_delete

from .models import Post


def garbage_collector(sender, instance, *args, **kwargs):
    if Post.objects.filter(content_id=instance.content_id):
        return

    instance.content.delete()


post_delete.connect(garbage_collector, sender=Post)
