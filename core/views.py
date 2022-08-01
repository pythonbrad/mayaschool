from django.shortcuts import render, redirect, get_object_or_404
from students.models import ClassStudent
from staffs.models import Staff
from .models import SubClass, Class
from finance.models import Invoice
from django.contrib.auth.decorators import login_required
from .forms import ClassForm


@login_required
def index(request):
    return render(request, 'core/dashboard.html', {
        'title': 'Dashboard',
        'current_page': 'dashboard',
        'nb_students': ClassStudent.objects.filter(
            session=request.current_session, student__status='active').count(),
        'nb_staffs': Staff.objects.filter(
            status='active').count(),
        'nb_classes': SubClass.objects.count(),
        'total_incomes': sum([
            invoice.total_amount_paid() for invoice in Invoice.objects.filter(
                session=request.current_session
            )
        ]),
    })


@login_required
def classes(request):
    classes = Class.objects.all()
    return render(request, 'core/classes_list.html', {
        'title': 'Classes',
        'current_page': 'setting.class.parent',
        'classes': classes,
    })


@login_required
def new_class(request):
    if request.POST:
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            pass
    else:
        form = ClassForm()
    return render(request, 'new_object.html', {
        'title': 'New class',
        'current_page': 'setting.class.parent',
        'form': form
    })


@login_required
def edit_class(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    if request.POST:
        form = ClassForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else:
            pass
    else:
        form = ClassForm(instance=obj)
    return render(request, 'new_object.html', {
        'title': 'Edit class',
        'current_page': 'setting.class.parent',
        'form': form,
    })


@login_required
def delete_class(request, pk):
    obj = get_object_or_404(Class, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('classes')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete class',
        'object': obj,
        'current_page': 'setting.class.parent',
    })

