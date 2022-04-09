from django.test import TestCase
from .models import Post, Comment


class TestPostModel(TestCase):
    """ Testing of a Post model """
    def test_post_title_unique(self):
        """ Test for a name to be set to unique """
        post = Post.objects.create(title='Mock Post')
        content = Post.objects.create(content='Some Content')
        self.assertEqual(str(tittle), 'Mock Post')
