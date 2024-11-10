from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
from .models import *

admin.site.register(Posts)
admin.site.register(Comments)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published' )
    list_editable = ('id', 'title', 'is_published' )