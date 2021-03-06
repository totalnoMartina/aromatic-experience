from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Status of the posts, so that if not ready to be published, is stored
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """ A model for post structure """
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    related_img = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='blog_posts')
    excerpt = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """ Using the order to be reversed for the most recent posts """
        ordering = ['-created']

    def __str__(self):
        """ A helper method for displaying the  """
        return f"A post named {self.title} was posted by {self.author}"

    def num_of_likes(self):
        """ A helper method to count the likes """
        return self.likes.count()


class Comment(models.Model):
    """ A model structure for comments """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ To create an order of comments, first are on top """
        ordering = ["created"]

    def __str__(self):
        """ A helper method to display data saved """
        return f"Comment {self.body} by {self.name}"
