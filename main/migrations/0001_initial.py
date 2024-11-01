# Generated by Django 5.1 on 2024-08-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=256, verbose_name='Slug')),
                ('photo_main', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Photo')),
                ('photo1', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Photo1')),
                ('photo2', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Photo2')),
                ('photo3', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Photo3')),
                ('photo4', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Photo4')),
                ('photo5', models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/d/', verbose_name='Photo5')),
                ('content', models.CharField(blank=True, max_length=3000, verbose_name='Контент')),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=1)),
            ],
        ),
    ]
