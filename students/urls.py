from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.index, name='students'),
    path('<int:pk>', views.details, name='student_details'),
    path('create', views.create, name='new_student'),
    path('<int:pk>/edit', views.edit, name='edit_student'),
    path('<int:pk>/delete', views.delete, name='delete_student'),
]
