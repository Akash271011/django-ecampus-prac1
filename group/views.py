from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def group(request):
    return HttpResponse("group called....")


def index(request):
    return render(request, 'group/index.html')
    
def contactUs(request):
    return render(request, 'group/contactUs.html')

def aboutus(request):
    return render(request, 'group/aboutus.html')