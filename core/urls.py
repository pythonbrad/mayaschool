from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('classes', views.classes, name='classes'),
    path('classes/create', views.new_class, name='new_class'),
    path('classes/<int:pk>/edit', views.edit_class, name='edit_class'),
    path('classes/<int:pk>/delete', views.delete_class, name='delete_class'),
    path('classes/child', views.subclasses, name='subclasses'),
    path('classes/child/create', views.new_subclass, name='new_subclass'),
    path('classes/child/<int:pk>/edit', views.edit_subclass, name='edit_subclass'),
    path('classes/child/<int:pk>/delete', views.delete_subclass, name='delete_subclass'),
]
