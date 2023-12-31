from django.contrib.auth.forms import UserCreationForm
from .models import User, ReviewRating
from django import forms


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review']