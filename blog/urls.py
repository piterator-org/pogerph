from django.urls import path

from . import views


urlpatterns=[
	path('',views.index,name='index'),
	path('article/<url_mark>/',views.article_detail,name='article_detail'),
]
