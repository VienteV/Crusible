from django.contrib.auth import get_user_model
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import AddPostForm, AddCommentForm
from .models import Posts, Likes, Comments, Comments_likes


# Create your views here.

def main(request):
    posts = Posts.objects.filter(is_published = 1)
    data = {'title': 'MainPage', 'posts': posts}
    return render(request, 'main/index.html', context=data)

class Main_view(ListView):
    template_name = 'main/index.html'
    context_object_name = 'query'
    def get_queryset(self):
        posts = Posts.objects.filter(is_published = 1)
        photos = ['photo1', 'photo2', 'photo3', 'photo4', 'photo5']
        for i in posts:
            i.photos = [i.__getattribute__(j) for j in photos]
            i.likes = Likes.objects.filter(post = i.pk)
            i.likes_amount  = Likes.objects.filter(post = i.pk).aggregate(Count('id'))
            i.last_comment = Comments.objects.filter(post=i.pk).last()
            if not(any(map(lambda a: bool(a), i.photos))):
                i.photos = False
            query = {'posts':posts, 'form': AddCommentForm}
        return query

    def post(self, request):
        try:
            post = Posts.objects.get(id = request.POST.get('post_id'))
            Likes.objects.create(user=request.user, post= post)
        except Exception as e:
            print(e)
        return redirect('/')


class Add_page(CreateView):
    form_class = AddPostForm
    model = Posts
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('main')


class Post_view(DetailView):
    model = Posts
    template_name = 'main/detail_post.html'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm
        context['comments'] = Comments.objects.filter(post=self.kwargs['pk'])
        return context

    #def post(self, request):
    #    text = request.POST.get('text')
    #    print(text)
    #   return redirect('main')

def add_comment(request):
    user = get_user_model().objects.get(username=request.POST.get('user'))
    post_pk = request.POST.get('post')
    post = Posts.objects.get(pk=post_pk)
    text = request.POST.get('text')
    Comments.objects.create(user=user, post=post, text=text)
    print(user, text, post)
    return redirect('post', post_pk)

def dell_post(request, pk):
    user = get_user_model().objects.get(username=request.user)
    post = Posts.objects.get(pk=pk)
    if user == post.autor:
        post.delete()
    return redirect('main')

def like_comment(request, post_id, comment_id):
    try:
        Comments_likes.objects.create(user=request.user, comment=Comments.objects.get(pk=comment_id))
    except:
        Comments_likes.objects.get(user=request.user, comment=Comments.objects.get(pk=comment_id)).delete
    return redirect('post', pk=post_id)