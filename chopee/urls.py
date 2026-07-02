from django.urls import path
from . import views


urlpatterns = [
    path('', views.chopee_index),
]
