from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
# Create your views here.

def home(request):
    
    student_data=Student.objects.all() 
    average=student_data.aaggregate(Avg('marks'))
    average=student_data.aaggregate(Sum('marks'))
    average=student_data.aaggregate(Min('marks'))
    average=student_data.aaggregate(Max('marks'))
    average=student_data.aaggregate(Count('marks'))
    
    print("Avg",average)
    print("Sum",Sum)
    print("max",Max)
    print("min",Min)  


      
    
    return render(request,'myapp/home.html',{'students':student_data})
    
    
