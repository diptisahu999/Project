from django.contrib import admin
from . models import Student,Emp,Mobile

# Register your models here.
@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','mobile']
    list_per_page=1
    search_fields=('name',)
    list_filter=('name',)
    
admin.site.register(Mobile)
admin.site.register(Emp)    
    
