from django import forms
from django.contrib.auth.models import User
from kickstartup.models import UserProfile, Industry, StartUp, Keywords

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = {'username', 'email', 'password'}

class UserProfileForm(forms.ModelForm):
    firstName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)