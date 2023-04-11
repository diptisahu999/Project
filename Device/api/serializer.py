from rest_framework import serializers
from api.models import Area,Department,SubArea,Devices,STBChannels,CroppedArea,Icon


class AreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields="__all__"
        
class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields="__all__"        
        
class SubAreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubArea
        fields="__all__"        
        
        
class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devices
        fields="__all__"  
        
        
class STBChannelListSerializer(serializers.ModelSerializer):
    class Meta:
        model=STBChannels
        fields="__all__"  

class CroppedAreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CroppedArea
        fields="__all__"
        
class IconListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Icon
        fields="__all__"