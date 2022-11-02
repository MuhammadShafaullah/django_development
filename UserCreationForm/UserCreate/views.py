from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
        messages.success(request,'signup sueccssfuly!')    
    else:
        fm=UserCreationForm()    
    return render(request,'app/signup.html',{'form':fm})
