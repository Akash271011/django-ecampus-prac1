from django.http import HttpResponse
from .models import Employee
from django.shortcuts import render
import email

# Create your views here.
def addEmployee(request):
    emp = Employee(ename='Ram',eage=25,eemail='ram@gmail.com',econtact=1234567890)
    emp.save()
    return HttpResponse("Employee Added.....")

def viewEmployee(request):
    employees = Employee.objects.all().values_list()
    print(employees)
    return render(request,'employee/view.html',{'employees':employees})

def deleteEmployee(request):
    emp = Employee.objects.get(id =6)
    emp.delete()
    return HttpResponse("Employee Deleted...")

def updateEmployee(request):
    emp = Employee.objects.get(id =6)
    emp.eage = 20
    emp.econtact = 456123789
    emp.save()
    return HttpResponse('Employee Updated...')
