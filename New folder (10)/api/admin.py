from django.contrib import admin
from .models import Electric_Product,Home_Kitchen_Product,Role

# Register your models here.
@admin.register(Electric_Product)
class UaseAdmin(admin.ModelAdmin):
    list_display=['id','mobile','tv','fan']
    

@admin.register(Home_Kitchen_Product)
class UaseAdmin(admin.ModelAdmin):
    list_display=['id','name']
    
@admin.register(Role)
class UaseAdmin(admin.ModelAdmin):
    list_display=['id','role_name','created_role_date','updated_role_date']