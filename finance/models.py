from django.db import models
from django.db.models import Sum
from core.models import AcademicSession, AcademicTerm
from students.models import Student
from django.utils import timezone


# Create your models here.
class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default=AcademicSession.get_current)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE, default=AcademicTerm.get_current)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("closed", "Closed")],
        default="active",
    )

    class Meta:
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
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()


class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    date_paid = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Receipt on {self.date_paid}"
