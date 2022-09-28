from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('aromaticblog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),

] 
