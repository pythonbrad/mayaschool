from core.models import AcademicSession
from .models import Student, ClassStudent
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm


@login_required
def index(request):
    return render(request, 'students/students_list.html', {
        'title': 'Students',
        'current_page': 'student',
        'class_students': ClassStudent.objects.filter(session=request.current_session)
    })


@login_required
def details(request, pk):
    return render(request, 'students/student_details.html', {
        'student': get_object_or_404(Student, pk=pk),
        'title': 'Student Details',
        'current_page': 'student',
    })


@login_required
def create(request):
    if request.POST:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            Student.objects.create(person=form.instance)
            ClassStudent.objects.create(
                subclass=SubClass.objects.get(pk=form.cleaned_data['current_class']),
                student=form.instance.student
            )
            return redirect('students')
        else:
            pass
    else:
        form = StudentForm()
    return render(request, 'new_object.html', {
        'title': 'New Student',
        'current_page': 'student',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.POST:
        form = StudentForm(request.POST, request.FILES, instance=obj.person)
        if form.is_valid():
            form.save()
            current_class = obj.get_current_class()
            current_class.subclass = SubClass.objects.get(pk=form.cleaned_data['current_class'])
            current_class.save()
            return redirect('students')
        else:
            pass
    else:
        form = StudentForm(instance=obj.person)
    return render(request, 'new_object.html', {
        'title': 'Edit Student',
        'current_page': 'student',
        'form': form
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('students')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete student',
        'object': obj,
        'current_page': 'student',
    })