from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.index, name='dashboard')
]
