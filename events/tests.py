from django.test import TestCase

from core.models import User
from ugc.models import Post, TextContent
from .models import Event


class TestEvents(TestCase):
    def setUp(self):
        print('START')
        self.author = User()
        self.author.username = 'user'
        self.author.save()

        self.text = TextContent()
        self.text.text = 'Test text'
        self.text.save()

    def test_creation_by_signal(self):
        post = Post()
        post.author = self.author
        post.content = self.text
        post.name = 'Post_name'
        post.save()

        event = Event.objects.get(event_content_id=post.pk)
        self.assertEqual(event.event_content, post)

        self.assertEqual(event.event_content_id, post.pk)
        self.assertEqual(event.author, self.author)

    def tearDown(self):
        print('END')
