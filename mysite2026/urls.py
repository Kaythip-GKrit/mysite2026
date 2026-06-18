
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def info(request):
    ip_adress = request.META['REMOTE_ADDR']
    res_text = f"Your IP Address is :{ip_adress}\n"
    
    for k, v in request.headers.items():
        res_text += f"<p>{k} :{v}</p>"
    return HttpResponse(res_text)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', info),
    path('', include('blog.urls')),
]
