from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.Register_user.as_view(), name='register'),
    path('prifile/<int:user_id>', views.profile, name='profile'),
    path('people/', views.Show_all_profiles.as_view(), name='people'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_photo/', views.AddPhoto.as_view(), name='add_photo'),
    path('chats/', views.ShowChats.as_view(), name='chats'),
    path('my_photo', views.ShowUserPhotos.as_view(), name='user_photos'),
    path('dell_photos/<int:photo_id>', views.dell_photo, name='dell_photo')
]
