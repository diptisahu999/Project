from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.TextField()
    mobile=models.CharField(max_length=5)
    password=models.CharField(max_length=5)
    created_at=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table='student_table'
        
class Mobile(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
        db_table='mobile_table'        

class Emp(models.Model):
    name=models.ForeignKey(Student,on_delete=models.CASCADE)
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    

    class Meta:
        db_table='emp_table'
        
