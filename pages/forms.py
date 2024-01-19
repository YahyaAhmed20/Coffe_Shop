from django import forms
from .models import SignUp
from .models import SignIn

class SignupForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields='__all__'


class SigninForm(forms.ModelForm):
    class Meta:
        model=SignIn
        
        fields='__all__'
        
        