from core.models import AcademicSession
from .models import Note
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Note.objects.filter(class_student__session=AcademicSession.get_current(), class_teacher__session=AcademicSession.get_current())
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
