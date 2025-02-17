from rest_framework.response import Response
from rest_framework.views import exception_handler

from utils.rest_framework.custom_exeption import CustomException


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    if isinstance(exc, CustomException):
        response = Response(
            exc.data,
            status=exc.status_code,
        )
    else:
        response = exception_handler(exc, context)
    return response
