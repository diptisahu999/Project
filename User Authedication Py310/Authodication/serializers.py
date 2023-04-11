from rest_framework import serializers 
from Authodication.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details



 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_Roles
        fields='__all__'
        
class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bms_User_Type
        fields='__all__'        
        
         
class TutorialSerializer(serializers.ModelSerializer):
    user_type_id=UserTypeSerializer(many=True,read_only=True)
    # role_id=RoleSerializer(many=True,read_only=True)
    class Meta:
        model = Bms_Users
        fields = '__all__'
        
class BmsUserDetailsSerializer(serializers.ModelSerializer):
    # user_id=UserTypeSerializer(many=True,read_only=True)
    role_id=RoleSerializer(many=True,read_only=True)
    user_id=TutorialSerializer(many=True,read_only=True)
    class Meta:
        model = Bms_Users_Details
        fields = '__all__'
