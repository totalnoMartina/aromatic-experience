""" A django module for testing """
import unittest
from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """ Testing details for Comment Form """

    def test_body_comment_required(self):
        """ Testing submitting of empty form """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')


if __name__ == '__main__':
    unittest.main()
