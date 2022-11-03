from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('profile/',views.profile,name='profile'),
]