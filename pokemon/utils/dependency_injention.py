from django.conf import settings

from pokemon.application.interfaces.user_repository import UserRepository
from pokemon.infraestructure.repositories.user_repository_db import DBUserRepository


def get_user_repository() -> UserRepository | None:
    """return an user repository instance"""
    if settings.USE_DB is True:
        return DBUserRepository()
