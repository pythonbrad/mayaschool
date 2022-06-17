from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'system_configs', views.SystemConfigViewSet)
router.register(r'sessions', views.AcademicSessionViewSet)
router.register(r'terms', views.AcademicTermViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'classes', views.ClassViewSet)
router.register(r'subclasses', views.SubClassViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
]
