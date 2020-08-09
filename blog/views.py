from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    return


def post(request, slug):
    return render(request, 'blog/post.html',
                  {'post': get_object_or_404(Post, slug=slug)})
