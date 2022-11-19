from urllib import request
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from minippa.models import user_contact
from django.contrib import messages
from .forms import SignUpForm,SignInForm,PostForm
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.core.cache import cache

# Create your views here.

def home(request):
  
    posts=Post.objects.all()
    return render(request,'minippa/home.html',{'posts':posts})
def about(request):
    return render(request,'minippa/about.html')

#contect model data saveing function
def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        massage=request.POST.get('desc')
        cn=user_contact(name=name,email=email,phone=phone,massage=massage)
        cn.save()
        messages.success(request, 'Massage Sent!')
        return render(request,'minippa/contact.html') 
    return render(request,'minippa/contact.html') 

# SignUp using django UserCreationForm
def sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            messages.info(request,'Signup Successfully!')
            return HttpResponseRedirect('/signup/')
    else:        
        fm=SignUpForm()
    return render(request,'minippa/signup.html',{'form':fm})

#SignIn useing django AuthenticationForm  and useing authenticate,login,
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignInForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                print(uname)
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in Sueccssfuly!') 
                    return HttpResponseRedirect('/profile/')  
        else:
            fm= SignInForm()
        return render(request,'minippa/signin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    
#Dashboard or user profile page after login 
def profile(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        ip=request.session.get('ip',0)
        ct=cache.get('count',version=user.pk)
        return render(request,'minippa/profile.html',{'posts':posts,'full_name':full_name,'grops':gps,'userIP':ip,'ct':ct})
    else:
        return HttpResponseRedirect('/signin/')

#django Logout useing authenticate,logout
def logoutt(request):
    logout(request)
    return HttpResponseRedirect('/home/')

#Add new post
# def addpost(request):
    if  not request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
            else:
                form=PostForm()    
            return render(request,'minippa/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/signin/')
        
#update post
def update(request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                
        else:
            pi=Post.objects.get(pk=id) 
            form = PostForm(instance=pi)            
        return render(request,'minippa/update.html',{'form':form})
    else:
        return HttpResponseRedirect('/signin/')
    
#Delete post
def deletepost(request ,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            posts=Post.objects.all()
            return render(request,'minippa/profile.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/signin/')    
    
def addpost(request):
    if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
            else:
                form=PostForm()    
            return render(request,'minippa/addpost.html',{'form':form})
    else:
        form=PostForm() 
    return render(request,'minippa/addpost.html',{'form':form})
          