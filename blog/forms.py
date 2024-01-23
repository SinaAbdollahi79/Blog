from django import forms
from blog.models import comment


class commentform(forms.ModelForm):

    class Meta:
        model=comment
        fields = ['post','name', 'subject', 'message', 'email']