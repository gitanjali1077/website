# this gives the generic user class
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import users

# u have to make a form for registration


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = users
        fields = ['username','email','password','college']

class UserForm2(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = User
        fields = ['username','email','password']

class UserForm1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = users
        fields = ['username','password']

        
class UserForm12(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = User
        fields = ['username','password']
