from django.http import HttpResponse

from nebulaspock.authorization.authenticateservice import validate_request


def authenticate_middleware(get_response):
    def middleware(request):
        # Code to be executed for each request/response after
        # the view is called.
        if validate_request(request):
            return get_response(request)  # response should be defined before
        else:
            return HttpResponse('Unauthorized request, Invalid credentials', status=401)

    return middleware
