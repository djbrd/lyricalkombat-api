from django import forms

class RhymeForm(forms.Form):
    rhyme = forms.CharField(label='Your rhyme', widget=forms.Textarea)