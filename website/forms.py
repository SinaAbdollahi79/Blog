from django import forms
from website.models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields = '__all__'
