from django.db import models
from django.utils.translation import gettext_lazy as _
# from model_utils import Choices

# Area Model
class Area(models.Model):
    name = models.CharField(max_length=150)

    def __str__ (self):
        return f'{self.name}'

    class Meta:
        db_table = 'area_tbl'
        
# Department Model
class Department(models.Model):
    name = models.CharField(max_length=150)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    def __str__ (self):
        return f'{self.name} - {self.area}'

    class Meta:
        db_table = 'department_tbl' 
        
# Sub Area Model
class SubArea(models.Model):
    name = models.CharField(max_length=150)
    on_image_path = models.CharField(max_length=255)
    off_image_path = models.CharField(max_length=255)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__ (self):
        return f'{self.name} - {self.department}'

    class Meta:
        db_table = 'subArea_tbl'

# Device Model
class Devices(models.Model):
    device_name = models.CharField(max_length=150)
    device_type = models.CharField(max_length=150)
    app_type = models.CharField(max_length=150)
    device_object = models.JSONField(default=dict, null=True, blank=True)
    sub_area = models.ForeignKey(SubArea,on_delete=models.CASCADE)

    def __str__ (self):
        return f'{self.device_name}'

    class Meta:
        db_table = 'devices_tbl'

# STB Channels Model
class STBChannels(models.Model):
    device = models.ForeignKey(Devices,on_delete=models.CASCADE)
    isOk = models.CharField(max_length=150)
    channels_object = models.JSONField(default=list, null=True, blank=True)
    
    def __str__ (self):
        return f'{self.device}'

    class Meta:
        db_table = 'STB_channels_tbl'
        
# Cropped Area Model
class CroppedArea(models.Model):
    device_name = models.CharField(max_length=150)
    crop_image_path =  models.CharField(max_length=255)
    moveto =  models.BooleanField()
    shape_type = models.CharField(max_length=150)
    isInteractive = models.BooleanField()
    crop_object = models.JSONField(default=dict, null=True, blank=True)
    sub_area = models.ForeignKey(SubArea,on_delete=models.CASCADE)
    index_number = models.IntegerField(null=True, blank=True)
    
    def __str__ (self):
        return f'{self.device_name}-{self.sub_area}'

    class Meta:
        db_table = 'cropped_area_tbl'
        

class Icon(models.Model):
    ICON_TYPES =(
        ("scenes_icons","Scene"),
        ("device_icons","Device"),
    )
    icon_id = models.IntegerField()
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    icon_type = models.CharField(max_length=150,choices=ICON_TYPES)
    
    def __str__ (self):
        return f'{self.name}'

    class Meta:
        db_table = 'icon_tbl'
    