from django import forms
from django.contrib.auth.models import User
from appone.models import UserProfileInfoForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    publicprofile = models.BooleanField(required=True)

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoForm
        fields = ('portfolio_site', 'profile_pic')

publicprofile = models.BooleanField(required=True)
