from django.contrib import admin
from .models import user_contact
from .models import Post

# Register your models here.
# Register your models here.
@admin.register(user_contact)
class user_contact(admin.ModelAdmin):
    list_display=('name','email','phone','massage')

@admin.register(Post)
class user_contact(admin.ModelAdmin):
    list_display=('id','title','desc')    
