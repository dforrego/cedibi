from django.utils.timezone import now
from rest_framework.response import Response


def response_data(message, status=200, extra_data=None):
    data = {'coderesponse': 0, 'message': message, 'date': now()}
    if extra_data:
        data.update(extra_data)
    return Response(status=status, data=data)

