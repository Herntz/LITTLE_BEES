# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom_complet', 'email', 'objet', 'message']
