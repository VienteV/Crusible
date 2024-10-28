from django import forms

from .models import Posts, Comments


class AddPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='Content')
    photo1 = forms.ImageField(required=False)
    photo2 = photo1
    photo3 = photo1
    photo4 = photo1
    photo5 = photo1
    class Meta:
        model = Posts
        fields = ['title', 'photo_main', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'content', 'is_published']

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['user', 'post', 'text', 'img']

