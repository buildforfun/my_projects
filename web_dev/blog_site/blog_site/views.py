from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for the Blog site"""
    return render(request, 'blog_site/index.html')