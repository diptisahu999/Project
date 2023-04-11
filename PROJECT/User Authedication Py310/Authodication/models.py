from django.db import models
from django.utils import timezone

# Create your models here.

class Bms_Module_master(models.Model):
    STATUS= [
        ("A","Active"),
        ("N","In-Active"),
    ]
    module_name=models.CharField(max_length=254)
    module_slug=models.CharField(max_length=254)
    status = models.CharField(max_length=100,choices=STATUS)
    created_module_date=models.DateTimeField(default=timezone.now)
    updated_module_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.module_name
    class Meta():
        db_table='bms_module_tbl'
        
        
class Bms_Roles(models.Model):
    role_name=models.CharField(max_length=100)
    created_role_date=models.DateTimeField(default=timezone.now)
    updated_role_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.role_name
    class Meta():
        db_table='bms_role_tbl'
  
  
        
class Bms_User_Type(models.Model):
    type_name=models.ManyToManyField(Bms_Roles,blank=True,related_name='aaa')
    created_user_type_date=models.DateTimeField(default=timezone.now)
    
    
    class Meta():
        db_table='bms_user_type_tbl'
        
        
class Bms_Users(models.Model):
    # user_type_id=models.ForeignKey(Bms_User_Type,on_delete=models.CASCADE)
    # role_id=models.ForeignKey(Bms_Roles,on_delete=models.CASCADE)
    user_type_id=models.ManyToManyField(Bms_User_Type,blank=True,related_name='movie')
    role_id=models.ManyToManyField(Bms_Roles,blank=True,related_name='song')
    user_email=models.EmailField()
    user_password=models.CharField(max_length=254)
    status = models.BooleanField(default=False)
    created_user_date=models.DateTimeField(default=timezone.now)
    updated_user_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_email
    class Meta():
        db_table='bms_user_tbl'
            
class Bms_Users_Details(models.Model):
    from Device.models import Bms_department_master,Bms_locker
    
    
    user_id=models.ManyToManyField(Bms_Users,related_name='abc')
    role_id=models.ManyToManyField(Bms_Roles,blank=True,related_name='xyz')
    department_id=models.ManyToManyField(Bms_department_master)
    locker_id=models.ManyToManyField(Bms_locker)
    first_name=models.CharField(max_length=254)
    last_name=models.CharField(max_length=254)
    image=models.ImageField(upload_to ='uploads/')
    phone_no=models.CharField(max_length=16)
    birthday=models.DateField(auto_now_add=True)
    address=models.TextField(max_length=2321)
    created_user_details_date=models.DateTimeField(default=timezone.now)
    updated_user_details_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
    class Meta():
        db_table='bms_user_details_tbl'
        
