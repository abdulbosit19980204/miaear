from django.shortcuts import render
from auth_app.models import User, MyUser
from django.db import connection
from tracker.views import fetch_data_from_raw_table
from .models import entities
from tracker.models import ChanelModel


def home_view(request):
    d = {}
    all_entities = entities.objects.all()
    print(MyUser.objects)
    my_user = MyUser.objects.filter(user=request.user).first()
    d['users'] = all_entities[:10]
    d['all_entities'] = all_entities.count()
    d['user'] = my_user,
    print(d['user'])
    return render(request, '../templates/Admin/index.html', context=d)


def user_home_view(request):
    return render(request, '../templates/User/index.html')


def channels_view(request):
    d = {}
    channels = ChanelModel.objects.all()
    d['channels'] = channels[:10]
    return render(request, '../templates/Admin/channels.html', context=d)
