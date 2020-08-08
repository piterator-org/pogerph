from django.shortcuts import render,get_object_or_404
from .models import Article,Menu,Button


def index(request):
	article_list=Article.objects.all().order_by('-publish_date')
	list_inline_item=Button.objects.all().order_by('order')
	navigation_menu_list=Menu.objects.all().order_by('order')
	return render(request,'blog/index.html',{'article_list':article_list,'list_inline_item':list_inline_item,'menu_list':navigation_menu_list})

def article_detail(request,url_mark):
	article=get_object_or_404(Article,link=url_mark)
	return render(request,'blog/article.html',{'article':article})
