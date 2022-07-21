from core.models import AcademicSession, AcademicTerm, SubClass
from .models import Staff
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StaffForm


@login_required
def index(request):
    return render(request, 'staffs/staffs_list.html', {
        'title': 'Staffs',
        'current_page': 'staff',
        'staffs': Staff.objects.filter()
    })


@login_required
def details(request, pk):
    return render(request, 'staffs/staff_details.html', {
        'staff': get_object_or_404(Staff, pk=pk),
        'title': 'Staff Details',
        'current_page': 'staff',
    })


@login_required
def create(request):
    if request.POST:
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            Staff.objects.create(person=form.instance)
            return redirect('staffs')
        else:
            pass
    else:
        form = StaffForm()
    return render(request, 'new_object.html', {
        'title': 'New Staff',
        'current_page': 'staff',
        'form': form
    })


@login_required
def edit(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    if request.POST:
        form = StaffForm(request.POST, request.FILES, instance=obj.person)
        if form.is_valid():
            form.save()
            current_class = obj.get_current_class()
            current_class.subclass = SubClass.objects.get(pk=form.cleaned_data['current_class'])
            current_class.save()
            return redirect('staffs')
        else:
            pass
    else:
        form = StaffForm(instance=obj.person)
    return render(request, 'new_object.html', {
        'title': 'Edit Staff',
        'current_page': 'staff',
        'form': form
    })


@login_required
def delete(request, pk):
    obj = get_object_or_404(Staff, pk=pk)
    if request.POST:
        obj.delete()
        return redirect('staffs')
    else:
        pass
    return render(request, 'delete_object.html', {
        'title': 'Delete staff',
        'object': obj,
        'current_page': 'staff',
    })
