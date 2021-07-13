from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    choices = [('Owner/Buyer', 'Owner/Buyer'),
               ('Builder', 'Builder'),
               ('Agent', 'Agent')]
    registered_as = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    class Meta:
        model = Profile
        fields = ['registered_as', 'contact_number', 'image']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    choices = [('Owner/Buyer', 'Owner/Buyer'),
               ('Builder', 'Builder'),
               ('Agent', 'Agent')]
    registered_as = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    class Meta:
        model = Profile
        fields = ['registered_as', 'contact_number', 'image']


