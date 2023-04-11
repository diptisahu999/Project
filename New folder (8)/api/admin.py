from django.contrib import admin
from .models import Student,Emplo,WEERE,Qwe

# Register your models here.
@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','mobile','email']
    
admin.site.register(Emplo)
admin.site.register(WEERE) 
admin.site.register(Qwe)    
   
    

