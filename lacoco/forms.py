from django import forms 
from .models import Profile

class InscriptionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Profile
        fields = ['username', 'password', 'email']