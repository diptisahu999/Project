from django.db import models



# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES= [
    ('F', 'Female'),
    ('M', 'Male'),
    ]

    STATUS_CHOICES= [
    ('A','Active'),
    ('N','Inactive'),
    ]
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    dob=models.DateField()
    address=models.TextField()
    gender=models.CharField(max_length=300, choices = GENDER_CHOICES)
    status=models.CharField(max_length=300, choices = STATUS_CHOICES)

    # def __str__(self):
    #     return f"{first_name} {last_name}"

    class Meta():
        db_table="employee_table"
