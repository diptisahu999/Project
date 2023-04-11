from rest_framework import serializers 

from Device.models import Bms_bulding_master,Bms_floor_master,Bms_department_master,Bms_sub_area_master,Bms_locker


class Bms_Bulding_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_bulding_master
        fields=['id','tower_name']
        
        
class Bms_floor_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_floor_master
        fields=['id','floor_name',]
        
        
class Bms_department_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_department_master
        fields=['id','department_name',]
        
        
class Bms_sub_area_master_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_sub_area_master
        fields=['id','sub_area_name','width','height','on_image_path','off_image_path']
        
        
class Bms_locker_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_locker
        fields=['id','locker_name','category','status','created_at','updated_at']