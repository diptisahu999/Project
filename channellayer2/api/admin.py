from django.contrib import admin
from .models import chat,Group

# Register your models here.
@admin.register(chat)
class ChatAdmin(admin.ModelAdmin):
    list_display=['id','content','timestamp','group']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=['id','name']
