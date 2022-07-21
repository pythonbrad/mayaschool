from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
	path('', views.index, name='staffs'),
	path('<int:pk>', views.details, name='staff_details'),
	path('create', views.create, name='new_staff'),
	path('<int:pk>/edit', views.edit, name='edit_staff'),
	path('<int:pk>/delete', views.delete, name='delete_staff'),
]
