from typing import Optional

from django.contrib.auth import authenticate

from pokemon.application.interfaces.user_repository import UserRepository
from pokemon.models.user import User


class DBUserRepository(UserRepository):
    def get_user(self, email: str) -> Optional[User]:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def create_user(self, email: str, password: str, name: str) -> User:
        user = User.objects.create_user(email=email, password=password, name=name)
        user.save()
        return user

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        return authenticate(email=email, password=password)
