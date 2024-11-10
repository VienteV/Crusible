from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Main_view.as_view(), name='main'),
    path('post/<int:pk>', views.Post_view.as_view(), name='post'),
    path('add_post', views.Add_page.as_view(), name='add_post'),
    path('post/add_comment', views.add_comment, name='add_comment'),
    path('dell_post/<int:pk>', views.dell_post, name='dell_post')
]