from django.urls import path
from .views import ListOfPosts, Detail, TheLikes, PostUpdate

urlpatterns = [
    path('', ListOfPosts.as_view(), name='home'),
    path('<slug:slug>/', Detail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', TheLikes.as_view(), name='edit_post'),
    path('update/<str:slug>/', PostUpdate, name='update_post'),
    # path('update/<slug:slug>/comment_id', views.update_comment, name='update_comment'),


]
