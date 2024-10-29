from django import forms
from .models import HelpLine

class HelpLineContact(forms.ModelForm):
    class Meta:
        model = HelpLine
        fields = ['name', 'email', 'issue']
        