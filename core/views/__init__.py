from django.shortcuts import render
from staffs.models import Staff
from ..models import SubClass
from django.contrib.auth.decorators import login_required
from . import classe, session, subclass, subject, term, system_config


__all__ = ['classe', 'session', 'subclass', 'subject', 'term']


@login_required
def index(request):
    return render(request, 'core/dashboard.html', {
        'title': 'Dashboard',
        'current_page': 'dashboard',
        'nb_students': request.current_session.classstudent_set.filter(
            student__person__status='active').count(),
        'nb_staffs': Staff.objects.filter(
            person__status='active').count(),
        'nb_classes': SubClass.objects.count(),
        'total_incomes': sum([
            invoice.total_amount_paid() for invoice in request.current_session.invoice_set.filter(
                status='active'
            )
        ]),
    })
