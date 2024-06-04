from typing import Optional

from pokemon.application.interfaces.user_repository import UserRepository
from pokemon.models.user import User
from pokemon.utils.dependency_injention import get_user_repository


class UserService:
    """handle all bussiness logic about the user"""

    def __init__(self):
        self.user_repository: UserRepository = get_user_repository()

    def get_user(self, email: str) -> Optional[User]:
        return self.user_repository.get_user(email)

    def create_user(self, email: str, password: str, name: str) -> User:
        return self.user_repository.create_user(email, password, name)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        return self.user_repository.authenticate_user(email, password)
