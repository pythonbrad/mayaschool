from django.urls import path
from . import views


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.index, name='dashboard'),
    path('classes', views.classe.index, name='classes'),
    path('classes/create', views.classe.create, name='new_class'),
    path('classes/<int:pk>/edit', views.classe.edit, name='edit_class'),
    path('classes/<int:pk>/delete', views.classe.delete, name='delete_class'),
    path('sessions', views.session.index, name='sessions'),
    path('sessions/create', views.session.create, name='new_session'),
    path('sessions/<int:pk>/edit', views.session.edit, name='edit_session'),
    path('sessions/<int:pk>/delete', views.session.delete, name='delete_session'),
    path('terms', views.term.index, name='terms'),
    path('terms/create', views.term.create, name='new_term'),
    path('terms/<int:pk>/edit', views.term.edit, name='edit_term'),
    path('terms/<int:pk>/delete', views.term.delete, name='delete_term'),
    path('modules', views.module.index, name='modules'),
    path('modules/create', views.module.create, name='new_module'),
    path('modules/<int:pk>/edit', views.module.edit, name='edit_module'),
    path('modules/<int:pk>/delete', views.module.delete, name='delete_module'),
    path('system_configs', views.system_config.index, name='system_configs'),
    path('system_configs/create', views.system_config.create, name='new_system_config'),
    path('system_configs/<int:pk>/edit', views.system_config.edit, name='edit_system_config'),
    path('system_configs/<int:pk>/delete', views.system_config.delete, name='delete_system_config'),
]
