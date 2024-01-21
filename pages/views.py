from django.shortcuts import render,redirect
from .models import SignUp
from .forms import SignupForm
from .forms import SigninForm
from .forms import SignIn
from .models import Product
# from .models import Signup
# Create your views here.



def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'pages/contact.html')

def menu(request):
  
    
  
    return render(request,'pages/menu.html',{'pro':Product.objects.all()})



def services(request):
    return render(request,'pages/services.html')

def signin(request):
    
    if request.method == 'POST':
            form = SigninForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                form = SigninForm()
    
    
    return render(request,'pages/signin.html',{'SI':SigninForm})

def signup(request):
    
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                form = SignupForm()
        return render(request,'pages/signup.html',{'SF':SignupForm})
                



    
    # dataform=SignupForm(request.POST)
    # dataform.save()
    # email=request.POST.get('email')
    # username=request.POST.get('username')
    # password =request.POST.get('password ')
    # data=SignUp(email=email,username=username,password=password)
    # data.save()
