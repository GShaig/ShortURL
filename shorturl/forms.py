from django import forms

from .models import Short

class ShortForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"placeholder": "Please enter your URL here"}))

    class Meta:
        model = Short
        fields = ('long_url',)
