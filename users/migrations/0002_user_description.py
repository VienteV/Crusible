# Generated by Django 5.1 on 2024-08-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=2000, null=True, verbose_name='Description'),
        ),
    ]
