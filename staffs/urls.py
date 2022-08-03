from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
	path('', views.index, name='staffs'),
	path('<int:pk>', views.details, name='staff_details'),
	path('create', views.create, name='new_staff'),
	path('<int:pk>/edit', views.edit, name='edit_staff'),
	path('<int:pk>/delete', views.delete, name='delete_staff'),
	path('class_titulars', views.class_titulars, name='class_titulars'),
	path('class_titulars/create', views.create_class_titular, name='new_class_titular'),
	path('class_titulars/<int:pk>/edit', views.edit_class_titular, name='edit_class_titular'),
	path('class_titulars/<int:pk>/delete', views.delete_class_titular, name='delete_class_titular'),
]
