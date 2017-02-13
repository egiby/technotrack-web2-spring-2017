from django.db import models

from core.models import Authored, Dated, Named


class Post(Authored, Dated, Named):
    text = models.TextField()

    def __str__(self):
        return self.name
