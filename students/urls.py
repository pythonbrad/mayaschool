from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.index, name='students_list'),
    path('<int:pk>', views.details, name='student_details'),
]
