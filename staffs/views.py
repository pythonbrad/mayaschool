from core.models import SubClass
from .models import Staff
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from .forms import StaffForm


@login_required
def index(request):
    return render(request, 'staffs/staffs_list.html', {
        'title': _('staffs_list').capitalize(),
        'current_page': 'staff',
        'staffs': Staff.objects.all()
    })


@login_required
def details(request, pk):
    return render(request, 'staffs/staff_details.html', {
        'staff': get_object_or_404(Staff, pk=pk),
        'title': _('staff_details').capitalize(),
        'current_page': 'staff',
    })


@login_required
def create(request):
    if request.POST:
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            Staff.objects.create(person=form.instance, diploma=form.cleaned_data['diploma'])
            return redirect('staffs')
        else:
            pass
    else:
        form = StaffForm()
    return render(request, 'object_form.html', {
        'title': _('add_staff').capitalize(),
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
            form.instance.staff.diploma = form.cleaned_data['diploma']
            form.instance.staff.save()
            return redirect('staffs')
        else:
            pass
    else:
        form = StaffForm(
            initial={
                'diploma': obj.diploma
            },
            instance=obj.person)
    return render(request, 'object_form.html', {
        'title': _('edit_staff').capitalize(),
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
        'title': _('delete_staff').capitalize(),
        'object': obj,
        'current_page': 'staff',
    })
