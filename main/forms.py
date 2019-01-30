from django.forms import ModelForm
from .models import Post
from django import forms

class PostComment(ModelForm):
    class Meta:
        model = Post
        fields = ('sender', 'text')
        widgets = {
            'sender': forms.TextInput(attrs={'placeholder': 'inserisci il tuo nome'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'scrivi il commento'}),
        }
        labels = {
            'sender': 'nome',
            'text': 'testo'
        }
