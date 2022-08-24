from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username"}),
            "password": forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your password"})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email"]
        help_texts = {
            "email": None,
            "username": None
        }
        widgets = {
            "username": forms.TextInput(),
            "email": forms.EmailInput()
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]