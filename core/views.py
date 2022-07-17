from django.shortcuts import render
from students.models import ClassStudent
from staffs.models import Staff
from .models import AcademicSession, SubClass
from finance.models import Invoice
from django.contrib.auth.decorators import login_required


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
