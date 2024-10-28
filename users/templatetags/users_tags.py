from django import template
from django.contrib.auth import get_user_model
from django.db.models import Q

from users.models import Chat

register = template.Library()

@register.inclusion_tag('users/profile_menu.html', takes_context=True)
def show_left_menu(context):
    print(str(context['request'].user))
    if str(context['request'].user) != 'AnonymousUser':
        print(1)
        user = context['request'].user
        print(get_user_model().objects.get(username=user).pk)
        menu = [{'name' : 'Мой профиль', 'url': 'profile', 'cur_user': get_user_model().objects.get(username=user).pk},
                {'name':'Мои фото', 'url':'user_photos'},
                {'name':'Мои диалоги', 'url': 'chats'}]
    else:
        menu =[]
    return {'menu': menu}