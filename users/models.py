from tkinter.constants import CASCADE

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import default
from django.urls import reverse_lazy


# Create your models here.
class User(AbstractUser):
    time_register = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/users/%Y/%m/%d', default='photos/users/user0.png', null=True, verbose_name='Photo')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Date birth')
    description = models.CharField(max_length=2000, null= True, verbose_name='Description')

class UserPhoto(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/users/%Y/%m/%d', default=None, null=False, verbose_name='Фотография')
    upload_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(null=True, default=None, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse_lazy('main')


class Chat(models.Model):
    user1 = models.ForeignKey("User", on_delete=models.CASCADE, related_name='user_1')
    user2 = models.ForeignKey("User", on_delete=models.CASCADE, related_name='user_2')

class Messages(models.Model):
    chat_id = models.ForeignKey("Chat", on_delete=models.CASCADE, related_name="chat")
    content = models.CharField(max_length=1000, null=False)
    sender = models.ForeignKey("User", on_delete=models.CASCADE,related_name='Sender')
    is_read = models.BooleanField(null=True)
    file = models.FileField(upload_to='photos/users/', null=True, default=False, verbose_name='Файл')
    time_sended = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering=['time_sended']