from django.shortcuts import render
from .models import Student

# Create your views here.

def studentData(request):

    students = Student.objects.all().values()
    students1 = Student.objects.filter(student_name__startswith='H').values()
    students2 = Student.objects.filter(student_name__contains='a').values()
    #lookup methods....
    #students3 = Student.objects.filter(role_id__gt=1).values() // taje integer filed like eg age....
    #students3 = Student.objects.filter(role_id__lte=1).values() // taje integer filed like eg age....
    print("filters",students2)
    print(students[0].get('id'))
    print(students[0])
    studentlist = []


    for i in students1[0].values():
        studentlist.append(i)

    print('student list',studentlist)

    #for student in students:
        #print(student.keys(),end='')
        #print(student.items())


    context = {
        'students': studentlist
    }
    return render(request, 'orm/student.html',context)
