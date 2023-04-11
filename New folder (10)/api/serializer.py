
from rest_framework import serializers
from . models import Electric_Product,Home_Kitchen_Product,Role


class Serializers(serializers.ModelSerializer):
    class Meta:
        model=Electric_Product
        fields="__all__"
        # fields=['name','email']    
    