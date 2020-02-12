from rest_framework.generics import RetrieveAPIView
from login.models import User
from login.serializers import LoginSerializer


# @csrf_exempt
# def login_user(request, pk):
#     try:
#         snippet = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = LoginSerializer(snippet)
#         return JsonResponse(serializer.data)


class UserList(RetrieveAPIView):
    queryset = User.objects.filter(pk=1)
    serializer_class = LoginSerializer
