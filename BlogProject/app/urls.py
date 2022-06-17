from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, post, contact, allblogs


urlpatterns = [
    path('', index),
    # path('blog/<slug:url>',post),
    path('post/<slug:url>',post),
    path('contact/', contact),
    path('allblogs/', allblogs)
]
