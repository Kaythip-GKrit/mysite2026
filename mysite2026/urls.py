from django.conf import settings
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render


# from . views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info),
    path('', views.home),
    path('index/', views.index),
    path('shopping', views.shopping),
    path('lucksoot/', views.lucksoot_pdf),
    path('chopee/', include('chopee.urls')),
]
