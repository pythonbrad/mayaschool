from .models import Invoice, InvoiceItem, Receipt
from rest_framework import serializers


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        exclude = []
        read_only_fields = [
            'session'
        ]


class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        exclude = []


class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        exclude = []
        read_only_fields = [
            'date_paid'
        ]
