from django.shortcuts import render
from .models import Student,Teacher
from django.db.models import Q

# Create your views here.

def home(request):
    # student_data=Student.objects.all()
    # student_data=Student.objects.get(pk=1) 
    # student_data=Student.objects.first() 
    # student_data=Student.objects.last() 
    # student_data=Student.objects.latest('pass_date')
    
    
    # one_data=Student.objects.get(pk=1)
    # student_data=Student.objects.earliest('pass_date')
    # print(student_data.filter(pk=one_data.pk).exists()) 
    
    # student_data,created=Student.objects.get_or_create(name='Sameer',roll=19,city='Multan',marks=80,pass_date='2020-5-6')
    # student_data=Student.objects.all()
    # print(created)
    
    # Student.objects.filter(marks=80).update(city="pass")  
    
    # student_data,created=Student.objects.update_or_create(id=14,name='shafa',roll=666,marks=65,pass_date='2020-4-5' ,defaults={'name':'kohli',})
    # print(created)
    # obj=[
    #     Student(name="ALi",roll=908,city="Isbd",marks=65,pass_date='2020-7-8'),
    #     Student(name="Osman",roll=945,city="Isbd",marks=65,pass_date='2020-7-8'),
    #     Student(name="Khos",roll=976,city="Isbd",marks=65,pass_date='2020-7-8')
    # ]
    # Student.objects.bulk_create(obj)
    
    # student_data=Student.objects.all()
    # for stu in student_data:
    #     stu.city='Karachi'
    # student_data=Student.objects.bulk_update(student_data,['city'])    
    student_data=Student.objects.in_bulk([1,2])
    print(student_data[2].name)
    
    return render(request,'myapp/home.html',{'students':student_data})
    
    
