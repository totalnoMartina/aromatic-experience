""" A django module for testing """
from django.test import TestCase
from .views import ListOfPosts, PostLike, Detail


class TestViews(TestCase):
