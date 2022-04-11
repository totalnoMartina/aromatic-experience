""" A django module for testing """
import unittest
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
from django.db import models
from django.test.utils import isolate_apps


class TestViews(TestCase):
    """ For testing the views functionality """
    @isolate_apps('aromaticblog')
    def get_posts(self):
        """ Test passes if display of posts is on a homepage """
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

if __name__ == '__main__':
    unittest.main()
