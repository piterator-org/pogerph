from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('post/<slug:slug>/', views.post, name='post'),
]
