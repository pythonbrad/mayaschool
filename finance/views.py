from core.models import AcademicSession
from .models import Invoice, InvoiceItem, Receipt
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    InvoiceSerializer, InvoiceItemSerializer, ReceiptSerializer
)


class InvoiceViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Invoice.objects.filter(session=AcademicSession.get_current())
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceItemViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = InvoiceItem.objects.filter(invoice__session=AcademicSession.get_current())
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReceiptViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Receipt.objects.filter(invoice__session=AcademicSession.get_current())
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]
