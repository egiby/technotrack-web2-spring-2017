from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import Authored


class Event(Authored):
    event_content_type = models.ForeignKey(ContentType)
    event_content_id = models.PositiveIntegerField(null=False, default=1)
    event_content = GenericForeignKey('event_content_type', 'event_content_id')

    def __str__(self):
        return 'Event from {}'.format(self.author)


class GeneratingEvent(models.Model):
    event = GenericRelation(Event,
                            content_type_field='event_content_type',
                            object_id_field='event_content_id',
                            on_delete=models.CASCADE
                            )
