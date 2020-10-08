import rest_framework.authtoken.views as authtoken_views
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class ObtainStyxAuthToken(authtoken_views.ObtainAuthToken):
    """post: Аутентификация. Принимает JSON с полями username, password,
             возвращает токен и данные о пользователе """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        groups = user.groups.all().values("id", "name")
        return Response({'token': token.key,
                         'user_id': user.id,
                         'roles': list(groups),
                         'first_name': user.first_name
                         })


class IsDeveloperUser(permissions.BasePermission):
    def has_permission(self, request, view):

        try:
            return request.user.is_superuser
        except:
            return False
