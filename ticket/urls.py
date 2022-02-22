
from django.urls import path,include
from .views import CreateTicket

urlpatterns = [
    
    path('add/', CreateTicket.as_view()),
    #path('view/',),

]