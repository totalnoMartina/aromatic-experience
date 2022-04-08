from . import views
from django.urls import path

urlpatterns = [
    path('', views.ListOfPosts.as_view(), name='home'),
    path('<slug:slug>/', views.Detail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]