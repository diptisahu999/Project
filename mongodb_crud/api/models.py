# from django.db import models
# from djongo import models
# from mongoengine import *
# from mongoengine import Document
# from .serializers import Serializers
# from djangotoolbox.fields import ListField
# from .forms import StringListField
# from djangotoolbox.fields import EmbeddedModelField

from djongo import models
# import tutorials.tbl_list as tbl_list

# class Tagline(models.Model):
#     is_turn_on = models.CharField(max_length=23)
    

class Tutorial(models.Model):
    name=models.CharField(max_length=23)
    email=models.EmailField()
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.CharField(max_length=200, blank=False, default='')
    
    
# class Dev(models.Model):
#     ss=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
#     name=models.CharField(max_length=23)
    # LED = models.EmbeddedField(model_container=Tagline)

    

    def __str__(self):
        return self.title
  
   

