from django.shortcuts import render
from . import models
# Create your views here.

def index(request,group_name):
    group=models.Group.objects.filter(name=group_name).first()
    chats=[]
    if group is None:
        group=models.Group.objects.create(name=group_name)
        group.save()
    else:
        chats=models.Chat.objects.filter(group=group)

    return render(request,'index.html',{'groupname':group_name,'chats': chats})