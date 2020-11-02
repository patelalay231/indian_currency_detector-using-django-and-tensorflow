from django import forms
from .models import Data

class Form(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('img', )