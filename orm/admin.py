from django.contrib import admin
from .models import Role, Employee,Student,Customer,Product,Order


# Register your models here.
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)


