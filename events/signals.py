from django.db.models.signals import post_save

from events.models import Event, GeneratingEvent


def generate_events(sender, instance, created=False, *args, **kwargs):
    if created:
        event = Event()
        event.author = instance.author
        event.event_content = instance
        event.save()


for clazz in GeneratingEvent.__subclasses__():
    post_save.connect(generate_events, sender=clazz)
