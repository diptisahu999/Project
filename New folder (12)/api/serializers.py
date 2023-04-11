from rest_framework import serializers
from . models import Student


class Serializers(serializers.ModelSerializer):
    name = serializers.ListField(min_length=0, max_length=1)
    class Meta:
        model=Student
        # fields="__all__"
        fields = ('name','email','mobile','password')
        # fields=['name','email']

        