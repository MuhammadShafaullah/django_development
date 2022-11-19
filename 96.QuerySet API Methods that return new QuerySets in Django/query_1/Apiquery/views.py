from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(request):
    student_data=Student.objects.all()
    #student_data=Student.objects.filter(marks=80)
    #student_data=Student.objects.exclude(marks=80)
    
    # student_data=Student.objects.order_by('name')
    # student_data=Student.objects.order_by('id').reverse()
    
    # student_data=Student.objects.order_by('id').reverse()[:5]
    
    # student_data=Student.objects.values()
    
    # student_data=Student.objects.values('name','city')
   
    # student_data=Student.objects.values_list('id','name',named=True)
    
    # student_data=Student.objects.using('default')
    # student_data=Student.objects.dates('pass_date','month')
    
    #######################Second Table####################
    
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Student.objects.values_list('id','name',named=True)
    # student_data=qs2.union(qs1)
    
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Student.objects.values_list('id','name',named=True)
    # student_data=qs2.union(qs1 ,all=True)
    
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Student.objects.values_list('id','name',named=True)
    # student_data=qs2.intersection(qs2)
    
    # qs1 = Student.objects.values_list('id','name',named=True)
    # qs2 = Student.objects.values_list('id','name',named=True)
    # student_data=qs2.difference(qs1)
 
 
########################### And OR Operater ########################

    # student_data=Student.objects.filter(id=9) & Student.objects.filter(marks=70)
    
    # student_data=Student.objects.filter(Q(id=9) & Q(marks=70)) 
    
    # student_data=Student.objects.filter(Q(id=9) | Q(marks=70)) 
    
    
    return render(request ,'myapp/home.html',{'students':student_data})
    
    
