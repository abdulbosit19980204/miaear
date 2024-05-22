from django.shortcuts import render
from auth_app.models import User, MyUser
from django.db import connection
from tracker.views import fetch_data_from_raw_table
from .models import entities, AdditionalSourcesModels
from tracker.models import ChanelModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_view(request):
    data = request.GET
    page = data.get('page', 1)
    visited = AdditionalSourcesModels.objects.filter(author=request.user).first()
    if visited is None:
        visit = AdditionalSourcesModels.objects.create(author=request.user, visitors=1)
        visit.save()
    visited.visitors += 1
    visited.save(update_fields=['visitors'])
    d = {}
    all_entities = entities.objects.all()
    d['users'] = Paginator(all_entities, 15).get_page(page)
    d['all_entities'] = all_entities.count()
    d['user'] = MyUser.objects.filter(user=request.user).first()
    d['visited'] = AdditionalSourcesModels.objects.filter(author=request.user).first()

    return render(request, '../templates/Admin/index.html', context=d)


def user_home_view(request):
    return render(request, '../templates/User/index.html')


def channels_view(request):
    d = {}
    channels = ChanelModel.objects.all()
    d['channels'] = channels[:10]
    d['user'] = MyUser.objects.filter(user=request.user).first()
    return render(request, '../templates/Admin/channels.html', context=d)


def users_view(request):
    d = {}
    users = MyUser.objects.all()
    d['user'] = MyUser.objects.filter(user=request.user).first()
    d['users'] = users[:10]
    return render(request, '../templates/Admin/users.html', context=d)
