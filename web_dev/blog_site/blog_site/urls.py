"""Defines URL patterns for blog_site"""

from django.urls import path

from . import views

app_name = 'blog_site'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),
]