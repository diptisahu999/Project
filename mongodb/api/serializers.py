from rest_framework import serializers
from . models import Student,Emp


class Serializers(serializers.ModelSerializer):
    names = serializers.ListField(source='email')
    # mobile = serializers.ListField(min_length=0, max_length=1)
    class Meta:
        model=Student
        # fields="__all__"
        fields = ('id','name','names','mobile','email','password')
        # fields=('name','mobile')
        # fields=['name','email']
    
        