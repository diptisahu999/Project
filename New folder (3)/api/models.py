from django.db import models

# Create your models here.
# from django.db import models
# from django.dispatch import receiver




# Create your models here.
class Consult(models.Model):
    name = models.CharField(max_length=16)
    subject= models.CharField(max_length=16, null=True)
    text = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    

    class Meta:
        db_table = 'Consult'

