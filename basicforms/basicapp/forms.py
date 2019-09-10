from django import forms
from django.core import validators
from basicapp.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    text = forms.CharField(widget=forms.Textarea)
