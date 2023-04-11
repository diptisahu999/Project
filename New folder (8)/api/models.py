from django.db import models

# Create your models here.
class Student(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
  
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)
    
class Emplo(Student):
    phone=models.CharField(max_length=12)
    
class WEERE(Student):
    salary=models.CharField(max_length=12)
    
class Qwe(Emplo):
    asa=models.CharField(max_length=23)
    
