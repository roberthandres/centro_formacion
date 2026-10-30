from django import forms
from .models import Aprendiz

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = '__all__'