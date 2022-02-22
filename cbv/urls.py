from django.contrib import admin
from django.urls import path,include
from .views import HrList

urlpatterns = [
    
    path('', HrList.as_view(), name='hr'),



]
