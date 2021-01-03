from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Order

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class signupform(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'email', 'password1','password2']

class loginform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']