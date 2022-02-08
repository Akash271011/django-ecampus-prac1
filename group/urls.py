from django.urls import path,include
from group import views

urlpatterns = [
    path('add/', views.group),
    path('contactUs/', views.contactUs),
    path('aboutus/', views.aboutus),
    path('', views.index),




]