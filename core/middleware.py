from .models import AcademicSession, AcademicTerm


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.get_current()
        current_term = AcademicTerm.get_current()

        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response
