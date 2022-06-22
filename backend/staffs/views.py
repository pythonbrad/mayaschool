from core.models import AcademicSession
from .models import Staff, ClassTeacher
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StaffSerializer, ClassTeacherSerializer


class StaffViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Staff.objects.all().order_by('-matricule')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClassTeacherViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = ClassTeacher.objects.filter(session=AcademicSession.get_current())
    serializer_class = ClassTeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
