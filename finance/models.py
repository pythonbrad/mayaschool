from django.db import models
from django.db.models import Sum
from core.models import AcademicSession, AcademicTerm
from students.models import Student
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("student"))
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current, verbose_name=_("session"))
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE, default=AcademicTerm.get_current, verbose_name=_("term"))
    status = models.CharField(
        max_length=20,
        choices=[("active", _("active").capitalize()), ("closed", _("closed").capitalize())],
        default="active", verbose_name=_("status")
    )

    class Meta:
        verbose_name = _('invoice').capitalize()
        ordering = ["student", "term"]

    def __str__(self):
        return f"{self.student}"

    def balance(self):
        payable = self.total_amount_payable()
        paid = self.total_amount_paid()
        return payable - paid

    def total_amount_payable(self):
        items = self.invoiceitem_set.aggregate(amount=Sum('amount'))
        return items['amount'] or 0

    def total_amount_paid(self):
        receipts = self.receipt_set.aggregate(amount=Sum('amount_paid'))
        return receipts['amount'] or 0


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name=_("invoice"))
    description = models.CharField(max_length=200, verbose_name=_("description"))
    amount = models.IntegerField(verbose_name=_("amount"))

    class Meta:
        verbose_name = _("invoice_item").capitalize()


class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name=_("invoice"))
    amount_paid = models.IntegerField(verbose_name=_("amount_paid"))
    date_paid = models.DateTimeField(default=timezone.now, verbose_name=_("date_paid"))
    comment = models.CharField(max_length=200, blank=True, verbose_name=_("comment"))

    def __str__(self):
        # Translators: We want inform the user about the date of payment
        return _(f"{self.date_paid}").capitalize()

    class Meta:
        verbose_name = _("receipt").capitalize()
