from core.models import AcademicSession
from .models import Student, ClassStudent
from django.shortcuts import render


def index(request):
    return render(request, 'students/students_list.html', {
        'title': 'Students',
        'class_students': ClassStudent.objects.filter(session=AcademicSession.get_current())
    })


def details(request):
    return render(request, 'students/student_details.html', {
        'title': 'Student Details'
    })
