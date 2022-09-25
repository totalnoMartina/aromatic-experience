from django.urls import path
from .views import ListOfPosts, Detail, TheLikes, PostUpdate, UsersDraftPost

urlpatterns = [
    path('', ListOfPosts.as_view(), name='home'),
    path('drafts/<str:username>', UsersDraftPost, name='drafts'),
    path('<slug:slug>/', Detail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', TheLikes.as_view(), name='post_like'),
    path('update/<str:slug>/', PostUpdate, name='edit_post'),
    # path('update/<slug:slug>/comment_id', views.update_comment, name='update_comment'),


]
