from django.contrib import admin
from .models import Consult

# Register your models here.
@admin.register(Consult)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name']
