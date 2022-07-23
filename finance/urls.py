from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.invoices, name='invoices'),
    path('invoice/<int:pk>', views.invoice_details, name='invoice_details'),
	path('invoice/create', views.create_invoice, name='new_invoice'),
	path('invoice/<int:pk>/edit', views.edit_invoice, name='edit_invoice'),
	path('invoice/<int:pk>/delete', views.delete_invoice, name='delete_invoice'),
	path('invoice/<int:pk>/receipt/create', views.create_receipt, name='new_receipt'),
	path('invoice/<int:id>/receipt/<int:pk>/edit', views.edit_receipt, name='edit_receipt'),
	path('invoice/<int:id>/receipt/<int:pk>/delete', views.delete_receipt, name='delete_receipt'),
]
