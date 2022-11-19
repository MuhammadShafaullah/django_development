
from django.contrib import admin
from django.urls import path
from hooks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('excp/',views.excp),
    path('user/',views.user_info),
    
    
]
