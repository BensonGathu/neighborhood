from django import forms
from .models import Neighborhood,UserProfile,Business,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'contact','email','id_number','hood']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post']


# class RegistrationForm(UserCreationForm):
#     contact = forms.IntegerField()
