from django.urls import path
from .views import ListOfPosts, Detail, TheLikes, PostUpdate, UsersDraftPost, DraftDetail, PostDelete

urlpatterns = [
    path('', ListOfPosts.as_view(), name='home'),
    path('drafts/<str:username>', UsersDraftPost.as_view(), name='drafts'),
    path('drafts_detail/<slug:slug>/', DraftDetail.as_view(), name='draft_detail'),
    path('<slug:slug>/', Detail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', TheLikes.as_view(), name='post_like'),
    path('edit_post/<slug:slug>/', PostUpdate.as_view(), name='edit_post'),
    path('delete_post/<slug:slug>/', PostDelete.as_view(), name='delete_post'),

    # path('update/<slug:slug>/comment_id', views.update_comment, name='update_comment'),


]
