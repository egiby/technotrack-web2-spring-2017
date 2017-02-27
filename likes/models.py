from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, \
    GenericRelation
from django.contrib.contenttypes.models import ContentType

from core.models import Authored, ImmutableDated


class Like(Authored, ImmutableDated):
    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_id')


class LikeAble(models.Model):
    likes = GenericRelation(Like, content_type_field='target_content_type',
                            object_id_field='target_id',
                            on_delete=models.CASCADE)

    class Meta:
        abstract = True
