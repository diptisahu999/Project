from django.db import models
from django.utils import timezone

# Create your models here.
    
    
class Electric_Product(models.Model):
    mobile=models.CharField(max_length=23)
    tv=models.CharField(max_length=23)
    fan=models.CharField(max_length=23)
    
    def __str__(self):
        return self.mobile
    class Meta():
        db_table='ele_tbl'
        
        
class Home_Kitchen_Product(models.Model):
    name=models.CharField(max_length=23)
    def __str__(self):
        return self.name
    class Meta():
        db_table='kit_product'
    
class Role(models.Model):
    role_name=models.CharField(max_length=100)
    assigned_devices=models.ManyToManyField(Electric_Product,blank=True)
    created_role_date=models.DateTimeField(default=timezone.now)
    updated_role_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role_name
    class Meta():
        db_table='role_tbl'    
    
