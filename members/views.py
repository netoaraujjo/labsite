# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    members = Member.objects.all()
    return render(request, 'members/index.html', {'members': members})
