from typing import Any

from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from pokemon.application.services.user_service import UserService
from pokemon.serializers.auth_serializer import AuthTokenSerializer
from pokemon.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = self.user_service.create_user(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
                name=serializer.validated_data["name"],
            )
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    serializer_class = AuthTokenSerializer

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = self.user_service.authenticate_user(
            serializer.validated_data["email"], serializer.validated_data["password"]
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})
