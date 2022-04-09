from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListOfPosts.as_view(), name='home'),
    path('<slug:slug>/', views.Detail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.TheLikes.as_view(), name='post_like'),
]