from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import User

class UserSignUpForm(UserCreationForm):
    username = forms.CharField(min_length=1, max_length=30, required=True, strip=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'User name'}))
    email = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email' }))
    name = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    photo = forms.ImageField(max_length=144, required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(min_length=1, max_length=60, required=True, strip=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'name', 'email', 'photo',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.save()
        return user

