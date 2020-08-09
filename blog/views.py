from readme_renderer import markdown, rst, txt

from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'startbootstrap-blog/home.html',
                  {'posts': Post.objects.all()})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.content = {
        'html': str,
        'md': markdown.render,
        'rst': rst.render,
        'txt': txt.render,
    }[post.markup](post.content)
    return render(request, 'startbootstrap-blog/post.html', {'post': post})
