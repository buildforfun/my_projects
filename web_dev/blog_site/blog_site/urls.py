"""Defines URL patterns for blog_site"""

from django.urls import path

from . import views

app_name = 'blog_site'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]