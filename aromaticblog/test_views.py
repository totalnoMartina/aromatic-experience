""" A django module for testing """
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from django.db import models
from django.test.utils import isolate_apps
# from .views import ListOfPosts, Detail, TheLikes


class TestViews(TestCase):
    """ For testing the views functionality """
    @isolate_apps('aromaticblog')
    def get_posts(self):
        """ Test passes if display of posts is on a homepage """
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_if_title_is_unique(self):
        class TestModel(models.Model):
            pass
        self.assertIs(self.apps.get_model('aromaticblog', 'TestModel'), TestModel)


