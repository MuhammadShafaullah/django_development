from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
from datetime import date,time
# Create your views here.

def home(request):
    
    student_data=Student.objects.all() 
    # student_data=Student.objects.filter(name__exact='Ali')
    
    # student_data=Student.objects.filter(name__iexact='Ali')
    
    # student_data=Student.objects.filter(name__contains='i')
    
    # student_data=Student.objects.filter(id__in=[1,3,6])
    
    # student_data=Student.objects.filter(marks__in=[80])
    # student_data=Student.objects.filter(marks__in=[80,70])
    
    # student_data=Student.objects.filter(marks__in=[80])
    
    # student_data=Student.objects.filter(marks__gt=80)
    # student_data=Student.objects.filter(marks__gte=80)
    
    # student_data=Student.objects.filter(marks__lt=[80])
    # student_data=Student.objects.filter(marks__lte=[80])
    
    #student_data=Student.objects.filter(name__startswith='s')
    # student_data=Student.objects.filter(name__istartswith='s')
    
    # student_data=Student.objects.filter(name__endwith='s')
    # student_data=Student.objects.filter(name__iendwith='s')
    
    # student_data=Student.objects.filter(passdate__range=('2020-04-01','2020-05-04'))
       
    # student_data=Student.objects.filter(admdatetime__date__gt=date(2020,4,5)) 
    
    # student_data=Student.objects.filter(passdate__month=4) 
    # student_data=Student.objects.filter(passdate__month__gte=4)
    # student_data=Student.objects.filter(passdate__day=4) 
    # student_data=Student.objects.filter(passdate__day__gt=4) 
    # student_data=Student.objects.filter(passdate__week=14)
    # student_data=Student.objects.filter(passdate__week__gt=14)
    # student_data=Student.objects.filter(passdate__week__day__gt=14)  
      
    
    return render(request,'myapp/home.html',{'students':student_data})
    
    
