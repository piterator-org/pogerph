from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'startbootstrap-blog/home.html',
                  {'posts': Post.objects.all()})


def post(request, slug):
    return render(request, 'startbootstrap-blog/post.html',
                  {'post': get_object_or_404(Post, slug=slug)})
