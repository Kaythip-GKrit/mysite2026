from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chopee_index(request):
    
    return render(request,'chopee_index.html')