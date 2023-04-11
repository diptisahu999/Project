from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

class Tasks(models.Model):
    name=models.CharField(max_length=23)
    description=models.TextField()
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.name


# def task_hendle(sender,instance,**kwargs):
#     print("you printed me")
#     print(instance.name)
#     print(instance.description)

# pre_save.connect(task_hendle,sender=Tasks)    