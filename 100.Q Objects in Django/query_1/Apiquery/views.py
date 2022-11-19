from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(request):
    
    # student_data=Student.objects.filter(Q(id=6)& Q(roll=1007))
    # student_data=Student.objects.filter(Q(id=6)| Q(roll=1007))
    student_data=Student.objects.filter(~Q(id=6))
    



      
    
    return render(request,'myapp/home.html',{'students':student_data})
    
    
