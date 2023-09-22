from django.contrib import admin
from . import models
# Register your models here.


class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id','content','group','timestamp']

class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(models.Chat,ChatModelAdmin)
admin.site.register(models.Group,GroupModelAdmin)