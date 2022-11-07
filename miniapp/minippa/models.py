from operator import mod
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class user_contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=70)
    massage=models.TextField(max_length=500)
    
class Post(models.Model):
    title=models.CharField(max_length=150) 
    desc=models.TextField()   
