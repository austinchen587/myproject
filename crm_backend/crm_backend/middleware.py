# crm_backend/middleware.py

from django.http import HttpResponseForbidden

class BlockHttpConnectMiddleware:
    """
    Middleware to block HTTP CONNECT requests.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "CONNECT":
            return HttpResponseForbidden("HTTP CONNECT method is not allowed.")
        return self.get_response(request)