from abc import ABC, abstractmethod
from typing import Optional

from pokemon.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_user(self, email: str) -> Optional[User]:
        """get user by email"""
        raise NotImplementedError

    @abstractmethod
    def create_user(self, email: str, password: str, name: str) -> User:
        """create an user"""
        raise NotImplementedError

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """authenticates the user"""
        raise NotImplementedError
