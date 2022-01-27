from django import forms
from .models import Registation


class RegistationForm(forms.ModelForm):

    class Meta:
        model = Registation
        fields = '__all__'
