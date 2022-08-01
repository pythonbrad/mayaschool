from core.models import AcademicSession
from .models import Student, ClassStudent
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StudentSerializer, ClassStudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Student.objects.all().order_by('-matricule')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClassStudentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = ClassStudent.objects.filter(session=AcademicSession.get_current())
    serializer_class = ClassStudentSerializer
    permission_classes = [permissions.IsAuthenticated]
