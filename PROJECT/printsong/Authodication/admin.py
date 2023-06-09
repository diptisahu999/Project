from django.contrib import admin
from Authodication.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details

# Register your models here.

@admin.register(Bms_Module_master)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','module_name','module_slug','status','created_module_date','updated_module_date']
    
    
@admin.register(Bms_Roles)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','role_name','created_role_date','updated_role_date']
    
@admin.register(Bms_User_Type)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','type_name','created_user_type_date']
    
    
@admin.register(Bms_Users)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','user_type_id','role_id','user_email','user_password','status','created_user_date','updated_user_date']

@admin.register(Bms_Users_Details)
class ModuleAdmin(admin.ModelAdmin):
    list_display=['id','user_id','role_id','first_name','image','phone_no','birthday','address','created_user_details_date','updated_user_details_date']