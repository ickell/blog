from django import forms
from .models import portfolio

class PostForm(forms.ModelForm):
    class Meta:
        model = portfolio
        fields = ['title', 'image', 'description']