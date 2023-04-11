from django.contrib import admin
from .models import Bms_bulding_master, Bms_floor_master, Bms_department_master, Bms_sub_area_master, Bms_locker, Bms_access_control_rfid_master, Bms_history, Bms_settings 

# Register your models here.
@admin.register(Bms_bulding_master)
class Bms_building_masterAdmin(admin.ModelAdmin):
    list_display=['id','tower_name','created_at','updated_at']
    
@admin.register(Bms_floor_master)
class Bms_floor_masterAdmin(admin.ModelAdmin):
    list_display=['id','floor_name','created_at','updated_at']
    
@admin.register(Bms_department_master)
class Bms_department_masterAdmin(admin.ModelAdmin):
    list_display=['id','department_name','created_at','updated_at']

@admin.register(Bms_sub_area_master)
class Bms_sub_area_masterAdmin(admin.ModelAdmin):
    list_display=['id','sub_area_name','on_image_path','off_image_path','width','height','seating_capacity','created_at','updated_at']

@admin.register(Bms_locker)
class Bms_lockerAdmin(admin.ModelAdmin):
    list_display=['id','locker_name','category','status','created_at','updated_at']

@admin.register(Bms_access_control_rfid_master)
class Bms_access_control_rfid_masterAdmin(admin.ModelAdmin):
    list_display=['id','rfid_no','card_type','status','access_start_time','access_end_time','created_at','updated_at']

@admin.register(Bms_history)
class Bms_historyAdmin(admin.ModelAdmin):
    list_display=['id','type','description','created_at']

@admin.register(Bms_settings)
class Bms_settingsAdmin(admin.ModelAdmin):
    list_display=['id','setting_data','created_at']
