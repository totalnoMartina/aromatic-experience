from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
from .models import Post
from .forms import CommentForm


class ListOfPosts(generic.ListView):
    """ Displaying posts on a landing page """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 6


class Detail(View):
    """ A view for details of the blog post """
    def get(self, request, slug, *args, **kwargs):
        """ A method to get posts and render all arguments """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "detail_view.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                'comment_form': CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
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


class PostLike(View):
    """ The view for the users to Like the posts/comments """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))