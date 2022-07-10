from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoice_items', views.InvoiceItemViewSet)
router.register(r'receipts', views.ReceiptViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
