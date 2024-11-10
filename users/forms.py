from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Messages, UserPhoto


class Register_form(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput())
    description = forms.CharField(label='Description', widget=forms.Textarea())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'photo', 'description']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords doesn't match")
        return cd['password1']

    def clean_email(self):
        cd = self.cleaned_data
        if get_user_model().objects.filter(email= cd['email']).exists():
            raise forms.ValidationError('This email already exist')
        else:
            return cd['email']

class Message_form(forms.ModelForm):
    file = forms.FileField(label='file',required=False)

    class Meta:
        model = Messages
        fields = ['content', 'file']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) <= 0:
            raise forms.ValidationError('Message shouldnt be empty')
        else:
            return content

class Addphoto_form(forms.ModelForm):

    class Meta:
        model = UserPhoto
        fields = ('photo', 'description')
