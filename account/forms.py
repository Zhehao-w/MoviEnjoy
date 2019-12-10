from django import forms
from account.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('gender','birthday','occupation', 'introduction','profile_pic')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserProfileInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('birthday','occupation', 'introduction')