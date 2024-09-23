from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegisterSerializer


class RegisterViewset(ViewSet):
    serializer_class = RegisterSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'token': str(refresh.access_token),
        }, status.HTTP_201_CREATED)