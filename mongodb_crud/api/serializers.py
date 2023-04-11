# from rest_framework import serializers
# from .models import Tagline



# class Serializers(serializers.ModelSerializer):
#     # names = serializers.ListField()
#     class Meta:
#         model=Tagline
#         fields="__all__"

from rest_framework import serializers 
from .models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = '__all__'
        

