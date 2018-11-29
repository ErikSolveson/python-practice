from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'AlexJo',
        'title': 'mount things',
        'content' : 'mostly dangerous and exciting things',
        'date_posted': 'Nov 14, 2018'
    },
    {
        'author': 'Jimmy Hepler',
        'title': 'Bugs',
        'content' : 'lots of gross creepy crawly things',
        'date_posted': 'Nov 15, 2018'
    }

]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
