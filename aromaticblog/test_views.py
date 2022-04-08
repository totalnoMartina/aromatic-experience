""" A django module for testing """
from django.test import TestCase
from .models import Post


class TestViews(TestCase):
    """ For testing the views functionality """

    
    def get_posts_display_in_homepage(self):
        """ Test passes if display of posts is on a homepage """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def get_posts_details_page(self):
        """ For testing if there is post rendering """
        post = Post.objects.create(content='New Test Content')
        response = self.client.get(f' {post.content}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail_view.html')
