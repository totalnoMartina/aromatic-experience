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

    def body_field_explicit_in_meta_class(self):
        """ Body is the main element, meta name should stay the same """
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body', ))