from django import forms
from django.forms import ModelForm

from facts.models import Fact


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    artist = forms.CharField(label='artist', max_length=100)
    song = forms.CharField(label='song', max_length=100)
    fact = forms.CharField(widget=forms.Textarea)


class FactCreateForm(ModelForm):
    class Meta:
        model = Fact
        fields = [
            'message',
            'author',
        ]