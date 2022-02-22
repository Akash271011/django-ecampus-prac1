from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def group(request):
    return HttpResponse("group called....")


def index(request):
    context ={
        'name' : 'FLIPKART'
    }
    return render(request, 'group/index.html' ,context)
    
def contactUs(request):
    context ={
        'contact_name' :["Kishan","Vinod","Rajesh","Sachin"]
    }
    return render(request, 'group/contactUs.html' ,context)

def aboutus(request):
    context = {
        'isActive' :True,
        'age':20,
    }
    return render(request, 'group/aboutus.html',context)