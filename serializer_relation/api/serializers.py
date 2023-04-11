from rest_framework import serializers
from .models import Singer,Song



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'  


class SingerSerializer(serializers.ModelSerializer):
    #song=serializers.StringRelatedField(many=True)
    #NESTED SERIALIZER
    song=SongSerializer(many=True)
    class Meta:
        model=Singer
        fields='__all__'