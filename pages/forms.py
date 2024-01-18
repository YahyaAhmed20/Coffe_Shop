from django import forms
from .models import SignUp



class SignupForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields='__all__'
        