from core.models import SubClass, Class
from .models import Student, ClassStudent
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm


@login_required
def index(request):
    return render(request, 'students/students_list.html', {
        'title': 'Students',
        'current_page': 'student',
        'class_students': request.current_session.classstudent_set.all()
    })


@login_required
def details(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_details.html', {
        'student': obj,
        'title': 'Student Details',
        'current_page': 'student',
        'payments': obj.invoice_set.all(),
    })


@login_required
def create(request):
    if request.POST:
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            Student.objects.create(person=form.instance, guardian=form.cleaned_data['guardian_name'])
            ClassStudent.objects.create(
                subclass=SubClass.objects.get(pk=form.cleaned_data['current_class']),
                student=form.instance.student
            )
            return redirect('students')
        else:
            pass
    else:
        form = StudentForm()
    return render(request, 'object_form.html', {
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
            form.instance.student.guardian = form.cleaned_data['guardian_name']
            form.instance.student.save()
            current_class = obj.get_current_class()
            if current_class.session == request.current_session:
                current_class.subclass = SubClass.objects.get(pk=form.cleaned_data['current_class'])
            else:
                ClassStudent.objects.create(
                    subclass=SubClass.objects.get(pk=form.cleaned_data['current_class']),
                    student=form.instance.student
                )
            current_class.save()
            return redirect('students')
        else:
            pass
    else:
        form = StudentForm(
            initial={
                "current_class": obj.get_current_class(),
                "guardian_name": obj.guardian
            },
            instance=obj.person)
    return render(request, 'object_form.html', {
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


@login_required
def generate_id_cards(request):
    data = request.current_session.classstudent_set.filter()
    options = {
        i.pk: {
            'name': i.name,
            'classes': {
                ii.pk: ii.name for ii in i.subclass_set.all()
            },
        } for i in Class.objects.all()
    }
    if request.GET:
        classe_id = request.GET.get('class', '')
        subclass_id = request.GET.get('subclass', '')
        if subclass_id.isdigit():
            data = data.filter(subclass_id=subclass_id)
        elif classe_id.isdigit():
            data = data.filter(subclass__parent_id=classe_id)
        else:
            pass

    return render(request, 'students/id_cards_list.html', {
        'title': 'ID Cards',
        'class_students': data,
        'current_page': 'student',
        'options': options,
    })
