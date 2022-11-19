
from django.shortcuts import render
from django.core.cache import cache
 

# Create your views here.
#way 1
# def home(request):
#     ml = cache.get('movie', 'has_expired')#agr moive name ky koi key h to wo ml mn set ho jaye ge otherwise 'has_expired' set ho jaye ga
#     print(ml)
#     if ml == 'has_expired':  #agr ml mn has_expired set h to 
#         cache.set('movie','The one',10) #moive key mn The Manjhi set ho jaye ga for 10 sec 
#         ml = cache.get('movie')
#         print(ml)
#     return render(request,'cache/home.html',{'fm':ml})

#way 2
def home(request):
    mv= cache.get_or_set('fees',6000,30,version=2)
    return render(request,'cache/home.html',{'fm':mv})


def contact(request):
    return render(request,'cache/contact.html')
