from django.db import models
from django.utils import timezone
from model_utils import Choices

# Create your models here.
class Role(models.Model):
    role_name=models.CharField(max_length=100)
    # assigned_devices=models.ManyToManyField(Devices,blank=True)
    created_role_date=models.DateTimeField(default=timezone.now)
    updated_role_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role_name
    class Meta():
        db_table='role_tbl'
        
class User(models.Model):
    USER_TYPES = Choices(
        ("A","Admin"),
        ("U","User"),
    )

    user_fname=models.CharField(max_length=150)
    user_lname=models.CharField(max_length=150)
    user_email=models.EmailField(max_length=254,unique=True)
    user_password=models.CharField(max_length=150)
    user_type=models.CharField(max_length=150,choices=USER_TYPES)
    role=models.ForeignKey(Role,on_delete=models.CASCADE,blank=True,null=True)
    created_user_date = models.DateTimeField(default=timezone.now)
    updated_user_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.user_fname
