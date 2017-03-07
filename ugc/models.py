from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from core.models import Authored, Dated, Named
from events.models import GeneratingEvent
from likes.models import Like, LikeAble


class Post(Authored, Dated, Named, LikeAble, GeneratingEvent):
    content_type = models.ForeignKey(ContentType)
    content_id = models.PositiveIntegerField(null=False, default=1)
    content = GenericForeignKey('content_type', 'content_id')

    def get_content(self):
        return self.content

    def __str__(self):
        return self.name


class Content(models.Model):
    post = GenericRelation(Post,
                           content_type_field='content_type',
                           object_id_field='content_id',
                           on_delete=models.CASCADE
                           )

    class Meta:
        abstract = True


# This is only the sample. We can do any other type of content.
class TextContent(Content):
    text = models.TextField()

    def __str__(self):
        return self.text[:10] + '...'

    class Meta:
        verbose_name = u'Text'
        verbose_name_plural = u'Texts'
