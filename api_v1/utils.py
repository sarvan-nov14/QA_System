from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    response = exception_handler(exc, context)
    if response is not None:
        if isinstance(exc, ValidationError):
            if isinstance(response.data, dict):
                response.data['error'] = "Validation Error"
        else:
            response.data['error'] = str(exc.detail)
        if isinstance(response.data, dict):
            response.data['status_code'] = response.status_code
            response.data['status_text'] = response.status_text
            response.data.pop('detail', None)

    return response
