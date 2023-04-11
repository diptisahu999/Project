from rest_framework import serializers
from . models import User,Role


class Serializers(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields="__all__"
    
        