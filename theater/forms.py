from django import forms
from .models import Play, Actor

class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ['title', 'description', 'date', 'actors', 'poster']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'actors': forms.SelectMultiple,
        }

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name', 'biography']
