from django import template

register = template.Library()

class Menu():
    def __init__(self, name, url, description=''):
        self.name = name
        self.url = url
        self.description = description

    def __str__(self):
        return self.name

@register.inclusion_tag('main/main_menu_tag.html', takes_context=True)
def show_menu(context):
    user = context['request'].user
    if 'user' in context['request']:
         user = context['request'].user
    else:
         ...
    menu =[Menu('Главная', 'main', description='Переход на главную страницу сейта'),
           Menu('Люди', 'people', description='Все пользователи'),]
    menu_if_login = [Menu('Добавить пост', 'add_post', description='Можно добавить свой пост'),
        Menu('Профиль', 'profile', description='Профиль пользователя'),
                        Menu('Выйти', 'logout', description='LogOut'),]
    menu_if_not_login = [ Menu('Регистрация', 'register', description='Переход в меню регистрации'),
                             Menu('Войти', 'login', description='Login'),]

    return {'menu': menu, 'menu_if_login':menu_if_login ,'menu_if_not_login':menu_if_not_login, 'user':user }

