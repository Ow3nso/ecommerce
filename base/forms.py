from dataclasses import fields

from django.forms import ImageField, ModelForm, TextInput, EmailInput, IntegerField

from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = "__all__"

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                }),
            'category': forms.Select(attrs={
                'class': "form-control", 
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control", 
                }),
            'price': TextInput(attrs={
                'class': "form-control", 
                }),
        }

class Inquireform(ModelForm):
    class Meta:
        model = Inquire
        fields = "__all__"



class Registerform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields = "__all__"
