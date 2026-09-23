from django.shortcuts import render,redirect
from .models import Student


def home(request):
    return render(request, 'home.html')

def dashboard(request):

    total_students = Student.objects.count()

    sixth = Student.objects.filter(
        student_class='6th'
    ).count()

    seventh = Student.objects.filter(
        student_class='7th'
    ).count()

    eighth = Student.objects.filter(
        student_class='8th'
    ).count()

    ninth = Student.objects.filter(
        student_class='9th'
    ).count()

    tenth = Student.objects.filter(
        student_class='10th'
    ).count()


    return render(
        request,
        'dashboard.html',
        {

        'total_students':total_students,

        'sixth':sixth,

        'seventh':seventh,

        'eighth':eighth,

        'ninth':ninth,

        'tenth':tenth

        }
    )



def student_list(request):

    search = request.GET.get('search')

    if search:

        students = Student.objects.filter(
            name__icontains=search
        )

    else:

        students = Student.objects.all()

    return render(
        request,
        'students_list.html',
        {
            'students': students
        }
    )

def add_student(request):

    if request.method=="POST":

        Student.objects.create(

            name=request.POST['name'],
            roll_no=request.POST['roll_no'],
            age=request.POST['age'],
            student_class=request.POST['student_class'],
            email=request.POST['email'],
            address=request.POST['address']

        )

        return redirect('/')

    return render(
        request,
        'add_students.html'
    )


def delete_student(request,id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('/students/')



def update_student(request,id):

    student = Student.objects.get(id=id)

    if request.method=="POST":

        student.name = request.POST['name']

        student.roll_no = request.POST['roll_no']

        student.age = request.POST['age']

        student.student_class=request.POST['student_class']

        student.email = request.POST['email']

        student.address = request.POST['address']

        student.save()

        return redirect('/students/')


    return render(
        request,
        'update_students.html',
        {'student':student}
    )

def class_students(request, class_name):

    students = Student.objects.filter(
        student_class=class_name
    )

    return render(
        request,
        'class_students.html',
        {
            'students': students,
            'class_name': class_name
        }
    )

def class_list(request):

    sixth=Student.objects.filter(
        student_class='6th'
    ).count()

    seventh=Student.objects.filter(
        student_class='7th'
    ).count()

    eighth=Student.objects.filter(
        student_class='8th'
    ).count()

    ninth=Student.objects.filter(
        student_class='9th'
    ).count()

    tenth=Student.objects.filter(
        student_class='10th'
    ).count()


    return render(
        request,
        'class_list.html',
        {

        'sixth':sixth,
        'seventh':seventh,
        'eighth':eighth,
        'ninth':ninth,
        'tenth':tenth

        }
    )


from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
Allow: /

Disallow: /dashboard/
Disallow: /students/
Disallow: /add/
Disallow: /update/
Disallow: /delete/
Disallow: /class/
Disallow: /class-list/
Disallow: /admin/

Sitemap: https://school-management.mpganes9.workers.dev/sitemap.xml     
"""

    return HttpResponse(content, content_type="text/plain")

from django.http import FileResponse
from pathlib import Path


from django.http import HttpResponse
from pathlib import Path
from django.conf import settings


def google_verification(request):
    file_path = settings.BASE_DIR / "school_project" / "google3ba06830d3fd2c2f.html"

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return HttpResponse(content, content_type="text/html")
