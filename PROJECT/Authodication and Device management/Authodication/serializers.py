from rest_framework import serializers 
from Authodication.models import Bms_Module_master,Bms_Roles,Bms_User_Type,Bms_Users,Bms_Users_Details


        
         
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bms_Users
        fields = '__all__'