from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate,login,logout  #for login

# Create your views here.

def signup(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account created sueccssfuly!')    
    else:
        fm=UserCreationForm()    
    return render(request,'app/signup.html',{'form':fm})

def signin(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'Password or Username error!')
    else:
        fm= AuthenticationForm()
    return render(request,'app/signin.html',{'form':fm})
  

def profile(request):
    
    return render(request,'app/profile.html') 
    
       
