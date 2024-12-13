from django.shortcuts import render

from .models import Post
from .utils import paginator


def index(request):
    template = 'index.html'
    return render(request, template)


def posts(request):
    template = 'posts.html'
    posts = Post.objects.order_by('-pub_date')
    page_obj = paginator(request, posts)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)