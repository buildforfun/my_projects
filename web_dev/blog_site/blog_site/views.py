from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """The home page for the Blog site"""
    return render(request, 'blog_site/index.html')

def topics(request):
    """Show a single topic"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'blog_site/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all it's entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topics':topics, 'entries':entries}
    return render(request, 'blog_site/topic.html', context)

