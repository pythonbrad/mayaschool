from .models import AcademicSession, AcademicTerm, SystemConfig


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.get_current()
        current_term = AcademicTerm.get_current()
        system_config = {i.key: i.value for i in SystemConfig.objects.all()}

        request.current_session = current_session
        request.current_term = current_term
        request.system_config = system_config

        response = self.get_response(request)

        return response
