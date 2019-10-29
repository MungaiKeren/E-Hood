from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


# Registration form
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["contacts", "image", "bio", "hood"]


class PostBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["name", "address", "image", "details", "hood"]


class PostNotice(forms.ModelForm):
    class Meta:
        model = Notices
        fields = ["title", "details", "hood"]


class AddFacility(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = ["name", "location", "image"]
