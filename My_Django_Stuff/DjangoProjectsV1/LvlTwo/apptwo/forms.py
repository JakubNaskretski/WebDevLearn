from django import forms
from apptwo.models import User

class UserForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'
