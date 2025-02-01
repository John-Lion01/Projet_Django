from django import forms
from .models import Reponse

class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['nom', 'email', 'age', 'commentaire']
