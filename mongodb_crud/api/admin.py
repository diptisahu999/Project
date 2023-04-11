from django.contrib import admin
from . models import Tutorial

# Register your models here.
@admin.register(Tutorial)
class UserAdmin(admin.ModelAdmin):
    list_display=['published']
    

# @admin.register(Tagline)
# class UserAdmin(admin.ModelAdmin):
#     list_display=['blog','title']    

    
