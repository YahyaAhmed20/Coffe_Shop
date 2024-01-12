from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'pages/contact.html')

def menu(request):
    return render(request,'pages/menu.html')



def services(request):
    return render(request,'pages/services.html')

def signin(request):
    return render(request,'pages/signin.html')

def signup(request):
    return render(request,'pages/signup.html')