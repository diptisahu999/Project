from django.contrib import admin

# Register your models here.
from .models import Role, User

# @admin.register(ActivationDetails)
# class ActivationDetailsAdmin(admin.ModelAdmin):
#     list_display = ('did','dname','purchase_code','mac_address','status','site_active_status')
#     search_fields = ("dname__startswith", )
#     list_per_page = 10

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['user_fname','user_lname','user_email','user_password','user_type','role','created_user_date','updated_user_date']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=['id','role_name','created_role_date','updated_role_date']