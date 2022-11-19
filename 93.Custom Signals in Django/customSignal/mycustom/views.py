from django.shortcuts import render,HttpResponse
from mycustom import signals
# Create your views here.

def home(request):
    signals.notification.send(sender=None,request=request,user=['Geeky','Show'])
    return HttpResponse("This is home page")
    