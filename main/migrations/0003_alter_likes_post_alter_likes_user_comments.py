# Generated by Django 5.1 on 2024-10-20 17:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Likes_post', to='main.posts'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Likes_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Text')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Img')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Coment_post', to='main.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Coment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
