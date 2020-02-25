from django.contrib import auth
from django.forms import model_to_dict
from django.http import HttpResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from oauth2_provider.decorators import protected_resource, rw_protected_resource
from rest_framework import authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from login.models import User
from login.serializers import UserSerializer, LoginSerializer


class UserList(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrTokenHasScope,)
    required_scopes = ['read']
    
    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs["pk"])
    
    
# @rw_protected_resource(scopes=['login'])
# @permission_classes([IsAuthenticatedOrTokenHasScope])
# @authentication_classes([authentication.TokenAuthentication])
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.get_authenticated_user()
        # user = LDAPBackend().authenticate(self, username, password)
        if user is not None and user.is_active and not user.is_staff:
            auth.login(request, user)
        else:
            return response_data(message='User not exist', status=400)

        data = UserSerializer(user)
        return response_data(message='success login', extra_data={'user': data.data})

    return response_data(message='Method not allow', status=405)


@api_view(['POST'])
@protected_resource(scopes=['write'])
# @permission_classes([IsAuthenticatedOrTokenHasScope])
def logout(request):
    if request.method == 'POST':
        if auth.get_user(request) is not None:
            auth.logout(request)
            return response_data(message='success logout')
        return response_data(message='User Not Exist', status=400)

    return response_data(message='Method not allow', status=405)


def response_data(message, status=200, extra_data=None):
    data = {'coderesponse': 0, 'message': message, 'date': now()}
    if extra_data:
        data.update(extra_data)
    return Response(status=status, data=data)