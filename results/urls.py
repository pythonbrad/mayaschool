from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.index, name='notes'),
    path('create', views.create, name='new_note'),
    path('<int:pk>/edit', views.edit, name='edit_note'),
    path('<int:pk>/delete', views.delete, name='delete_note'),
    path('report_cards', views.generate_report_cards, name='report_cards'),
]
