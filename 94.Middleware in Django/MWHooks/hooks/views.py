from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse 

# Create your views here.

def home(request):
    print("I am view")
    return HttpResponse("its home page")
def excp(request):
    print("I am  Excp view")
    a= 10/0
    return HttpResponse("This excp page")

def user_info(request):
    print("I am user info view")
    contecxt={'name':'Rahul'}
    return TemplateResponse (request,'hooks/tempMW.html',contecxt)
