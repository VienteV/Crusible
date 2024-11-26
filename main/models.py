from tkinter.constants import CASCADE

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


# Create your models here.
User = get_user_model()
class Posts(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    autor = models.ForeignKey('users.user', on_delete=models.CASCADE, null=True, related_name='Posts')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    slug = models.SlugField(max_length=256, verbose_name='Slug')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True,default=None, null=True, verbose_name='Photo')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True, default=None, null=True, verbose_name='Photo1')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True, default=None, null=True, verbose_name='Photo2')
    photo3 = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True, default=None, null=True, verbose_name='Photo3')
    photo4 = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True, default=None, null=True, verbose_name='Photo4')
    photo5 = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True, default=None, null=True, verbose_name='Photo5')
    content = models.CharField(max_length=3000, blank=True, verbose_name='Контент')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering=['time_created']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Likes(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='Likes_post')
    user = models.ForeignKey('users.User',  on_delete=models.CASCADE, related_name='Likes_user')

    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(post=self.post, user=self.user).exists():
            self.__class__.objects.filter(post=self.post, user=self.user).delete()
            raise Exception("Запись с такими значениями уже существует")
        else:
            super().save(*args, **kwargs)

class Comments(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='Coment_user')
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='Coment_post')
    text = models.CharField(max_length=500, verbose_name='Text')
    img = models.ImageField(upload_to='photos/%Y/%m/d/', blank=True, default=None, null=True, verbose_name='Img')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['time_created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Comments_likes(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments_likes_user')
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE, related_name='comments_likes_comment')

    def save(self, *args, **kwargs):
        if self.__class__.objects.filter(comment=self.comment, user=self.user).exists():
            raise Exception("Запись с такими значениями уже существует")
        else:
            super().save(*args, **kwargs)