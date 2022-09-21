import http
import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from apps.oxxo.models import COxxos


def myfirstview(request):
    data={
        'title':'Test',
        'oxxos': COxxos.objects.all()
    }
    return render(request,'catalogos/recursos/list.html',data)

