from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from .models import Post, Comment, ContactUser
from .forms import CommentForm, PostForm, ContactUserForm
from django.views.generic.edit import DeleteView


class ListOfPosts(View):
    """ Displaying posts on a landing page """
    def get(self, request, *args, **kwargs):
        post_list = Post.objects.all().filter(status=1).order_by('-created')
        return render(request, 'index.html', {'post_list': post_list})
        


class UsersDraftPost(View):
    """ A view for the list of drafted posts """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post_author = get_object_or_404(User, username=kwargs['username'])
            drafts_list = Post.objects.all().filter(
                status=0, author=post_author
            ).order_by('-created')
            context = {
                'drafts_list': drafts_list,
            }
            return render(request, 'drafts.html', context)


class DraftDetail(View):
    """ A view for the draft details rendering """
    def get(self, request, *args, **kwargs):
        current_user = get_object_or_404(User, username=kwargs['username'])
        draft_post = get_object_or_404(Post, slug=kwargs['slug'])
        if draft_post.author == current_user:
            return render(request, 'draft_detail.html', {'draft_post': draft_post})

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
            # Alert user with django messages
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

class PostAdding(View):
    """ Creating view class """
    def get(self, request, *args, **kwargs):
        """ A function to render form for adding posts """
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'add_post.html', context)

    def post(self, request, *args, **kwargs):
        """ Handling post request """
        form = PostForm(request.POST, request.FILES)
        user = get_object_or_404(User, username=request.user.username)
        if form.is_valid():
            # Cancel the save method temporarily
            post = form.save(commit=False)
            # put user in the field author from request
            post.author = request.user
            #save form
            post.save()
            return HttpResponseRedirect('/drafts/{}'.format(user.username))
        else:
            form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'add_post.html', context)


class PostUpdate(View):
    """ Updating view class """
    def get(self, request, *args, **kwargs):
        """ A function to get the data of existing post from an author and put it into form """
        post = get_object_or_404(Post, slug=kwargs['slug'])
        if post.status == 0:
            form = PostForm(instance=post)
            context = {
                'post': post,
                'form': form
            }
            return render(request, 'edit_post.html', context)

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form.save()
            current_user = get_object_or_404(User, username=kwargs['username'])
            return HttpResponseRedirect('/drafts_detail/{username}/{slug}/'.format(username = current_user.username, slug = post.slug))
        else:
            form = PostForm(request.POST, request.FILES, instance=post)
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'edit_post.html', context)
        
        # if request.user.is_superuser or request.user.id == post.author.id:

class PostDelete(DeleteView):
    """ A class to delete posts that are in draft """
    def get(self, request, *args, **kwargs):
        """ A function to get the data of existing post from an author and put it into form """
        post = get_object_or_404(Post, slug=kwargs['slug'])
        if post.status == 0:
            print('this is deleting printing post')
            context = {
                'post': post,
            }
            return render(request, 'post_confirm_delete.html', context)
    def post(self, request, *args, **kwargs):
        """ Getting the post data and prefilled form to be deleting them"""
        post = get_object_or_404(Post, slug=kwargs['slug'])
        user = get_object_or_404(User, username=request.user.username)
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return HttpResponseRedirect('/drafts/{}'.format(user.username))  


def contact_page(request):
    """ A view to return homepage """
    form = ContactUserForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Thanks for reaching out!')
        post_list = Post.objects.all().filter(status=1).order_by('-created')
        return render(request, 'index.html', {'post_list': post_list})
    context = {
            'form': form
        }
    return render(request, 'contact_form.html', context)


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


