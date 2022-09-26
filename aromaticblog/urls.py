from django.urls import path
from .views import ListOfPosts, Detail, TheLikes, PostUpdate, UsersDraftPost, DraftDetail, PostDelete, PostAdding

urlpatterns = [
    path('', ListOfPosts.as_view(), name='home'),
    path('drafts/<str:username>', UsersDraftPost.as_view(), name='drafts'),
    path('drafts_detail/<str:username>/<slug:slug>/', DraftDetail.as_view(), name='draft_detail'),
    path('<slug:slug>/', Detail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', TheLikes.as_view(), name='post_like'),
    path('add_post/<str:username>/', PostAdding.as_view(), name='add_post'),
    path('edit_post/<str:username>/<slug:slug>/', PostUpdate.as_view(), name='edit_post'),
    path('post_confirm_delete/<str:username>/<slug:slug>/', PostDelete.as_view(), name='post_confirm_delete'),
]
    # path('update/<slug:slug>/comment_id', views.update_comment, name='update_comment'),
