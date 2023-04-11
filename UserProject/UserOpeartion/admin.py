from django.contrib import admin
from UserOpeartion.models import Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','age','dob','address','status')
    search_fields=("first_name","last_name")
    list_filter=("dob",)
    list_per_page=2


# Register your models here.python
