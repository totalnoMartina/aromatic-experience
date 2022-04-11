from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


class ListOfPosts(generic.ListView):
    """ Displaying posts on a landing page """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 4


class Detail(View):
    """ For rendering details of the blog post """
    def get(self, request, slug, *args, **kwargs):
        """ A method to get posts and render filtering by status """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        # Comments are filtered in order by most recent and published
        comments = post.comments.filter(approved=True).order_by("-created")
        liked = False
        # Only users who are logged in can like
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "detail_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ A method for getting the comments and request approval """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created")
        liked = False  # Originally comments are not 'liked'
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True  # Users that have a profile can like

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # Using module django messages
            messages.add_message(request, messages.SUCCESS, 'Thank you, your comment matters!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "detail_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

# class UpdateComment(UpdateView):
#     model = Comment
#     template_name = 'update_comment.html'
#     form_class = UpdateComment

class TheLikes(View):
    """ The view for the users to Like the posts or comment """
    def post(self, request, slug, *args, **kwargs):
        """ Connecting to a particular post by slug """
        post = get_object_or_404(Post, slug=slug)
        # If there is likes already, clicking deletes it
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            # If user did not like yet, add like
            post.likes.add(request.user)
        # Redirecting to the post detail page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
