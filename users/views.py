from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.files.uploadedfile import UploadedFile
from django.db.models import Q
from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from .forms import Register_form, Message_form, Addphoto_form
from .models import Chat, Messages, UserPhoto


# Create your views here.
class Register_user(CreateView):
    template_name = 'users/register_user.html'
    form_class = Register_form
    success_url = reverse_lazy('main')

def profile(request, user_id):
    user = get_user_model().objects.filter(pk= user_id)
    print(request.user)
    photos = UserPhoto.objects.filter(user=user_id)
    di = {'user_profile': user[0], 'photos': photos}
    return render(request, 'users/profile.html', context = di)

def dell_photo(request, photo_id):
    print(request.user)
    cur_user = get_user_model().objects.filter(username= request.user)
    photo = UserPhoto.objects.get(pk=photo_id)
    print(photo.user, request.user)
    if photo.user == request.user:
        photo.delete()
    return redirect('user_photos')

class Show_all_profiles(ListView):
    template_name = 'users/people.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return get_user_model().objects.all()

def chat(request, user_id):
    current_user = request.user
    if current_user.is_authenticated:
        if Chat.objects.filter(Q(user1=current_user.pk) & Q(user2=user_id) | Q(user1=user_id) & Q(user2=current_user.pk)).exists():
            chat_object = Chat.objects.filter(Q(user1=current_user.pk) & Q(user2=user_id) | Q(user1=user_id) & Q(user2=current_user.pk))[0]
        else:
            Chat.objects.create(user1=current_user, user2= get_user_model().objects.get(pk=user_id))
            chat_object = Chat.objects.filter(
                Q(user1=current_user.pk) & Q(user2=user_id) | Q(user1=user_id) & Q(user2=current_user.pk))[0]

    if request.method == "POST":
        content = request.POST['content']
        form = Message_form(request.POST, request.FILES)
        data = dict(form.data.copy())
        data = dict(list(data.items()) + list({'chat_id':chat_object, 'sender':current_user, 'is_read':False}.items()))
        form.data = data
        form.save()
        #Messages.objects.create(chat_id=chat_object, content=content, sender=current_user, file=file, is_read=False)
        return redirect('chat', user_id=user_id)

    else:
        form = Message_form
    messages = Messages.objects.filter(chat_id = chat_object.pk)
    user = get_user_model().objects.get(pk=user_id)
    return render(request, 'users/chat.html', context={'chat':chat_object, 'messages': messages, 'form':form, 'user':user})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login_user.html'
    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('main')

class AddPhoto(CreateView):
    form_class = Addphoto_form
    template_name = 'users/add_photo.html'

    def form_valid(self, form):
        p = form.save(commit=False)
        print(self.request.user, 'aaaaa')
        p.user = self.request.user
        return super().form_valid(form)

class ShowChats(ListView):
    template_name = 'users/chats.html'
    context_object_name = 'chats'

    def get_queryset(self):
        user = self.request.user
        chats = Chat.objects.filter(Q(user1 = user)| Q (user2 = user))
        all_chats = []
        for chat in chats:
            print(chat.pk)
            user2 = chat.user1 if chat.user1 != user else chat.user2
            all_chats.append({"user":user2, 'chat':chat})
        return all_chats

class ShowUserPhotos(ListView):
    template_name = 'users/user_photos.html'
    context_object_name = 'photos'
    def get_queryset(self):
        user = self.request.user
        return UserPhoto.objects.filter(user = user)