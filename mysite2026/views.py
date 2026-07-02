
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
# def info(request):
#     ip_adress = request.META['REMOTE_ADDR']
#     res_text = f"Your IP Address is :{ip_adress}\n"
    
#     for k, v in request.headers.items():
#         res_text += f"<p>{k} :{v}</p>"
#     return HttpResponse(res_text)

def home(request):
    return render(request,'home.html',)
def index(request):
    return render(request,'index.html',)

def info(request):
    data = {}
    print('request.META')
    for k,v in request.META.items():
        data[str(k)] = str(v) 
        print(k, '=',v)
    return JsonResponse(data)
def shopping(request):
    return render(request, 'shopping.html')

def lucksoot_pdf(request):
    filepath = settings.BASE_DIR / 'lucksoot.pdf'
    return FileResponse (
        open(filepath, 'rb'),
        content_type = 'application/pdf',
        filename='lucksoot.pdf'
    )

