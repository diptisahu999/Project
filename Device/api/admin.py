from django.contrib import admin
from api.models import Area,Department,SubArea,Devices,STBChannels,CroppedArea,Icon

# Register your models here.
admin.site.register(Area)
admin.site.register(Department)
admin.site.register(STBChannels)
admin.site.register(SubArea)
admin.site.register(Devices)
admin.site.register(CroppedArea)
admin.site.register(Icon)


