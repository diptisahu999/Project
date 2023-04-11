from rest_framework import serializers 
from Authodication.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details
from Device.models import Bms_department_master,Bms_locker



 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_Roles
        fields=['role_name']
        
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_User_Type
        fields='__all__'        
        
        
class DepertmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_department_master
        fields=['department_name'] 
        
class lockerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_locker
        fields=['locker_name']
         
class BmsUserSerializer(serializers.ModelSerializer):
    # user_type_id=UserTypeSerializer(many=True,read_only=True)
    role_id=RoleSerializer(many=True,read_only=True)
    department_id=DepertmentSerializer(many=True,read_only=True)
    locker_id=lockerSerializer(many=True,read_only=True)
    class Meta:
        model = Bms_Users_Details
        fields = '__all__'
        
class BmsUserDetailsSerializer(serializers.ModelSerializer):
    # user_type_id=UserTypeSerializer(many=True,read_only=True)
    role_id=RoleSerializer(many=True,read_only=True)
    user_details=BmsUserSerializer(many=True,read_only=True)
    
    class Meta:
        model = Bms_Users
        fields = '__all__'
