from itertools import count

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
from .models import *

admin.site.register(Comments)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    fields = ('autor', 'title', 'is_published', 'photo_main')
    list_display = ('id', 'title', 'is_published' )
    list_editable = ('is_published', )
    list_display_links = ('title',)
    search_fields = ['title']
    list_per_page = 10
    actions = ['set_published',]

    @admin.action(description="Set Published")
    def set_published(self, request, queryset):
        count =queryset.update(is_published=Posts.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Set Draft")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Posts.Status.DRAFT)
        self.message_user(request, f'Изменено {count} записей')