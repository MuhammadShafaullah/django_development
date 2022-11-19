
from django.contrib import admin
from django.urls import path,include
from minippa import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.sign_up,name='signup'),
    path('signin/',views.sign_in,name='signin'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logoutt,name='logout'),
    path('addpost/',views.addpost,name='addpost'),
    path('deletepost<int:id>/',views.deletepost,name='deletepost'),
    path('update<int:id>/',views.update,name='update')
]


