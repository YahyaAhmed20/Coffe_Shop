from django.shortcuts import render
from .models import Signup
from .forms import SignupForm
# Create your views here.


def signup(request):
    return render(request,'pages/signup.html')
