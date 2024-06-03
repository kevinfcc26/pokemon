from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class BaseRepository(ABC):

    @abstractmethod
    def create(self, entity: T) -> T:
        """Create new entity

        Args:
            entity (T): entity to create

        Returns:
            T: entity created
        """
        raise NotImplementedError

    @abstractmethod
    def read(self, item_id: int) -> T:
        """Return an entity by id

        Args:
            item_id (int): entity id

        Returns:
            T: return entity
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id, entity):
        """update and entity

        Args:
            item_id (_type_): entity id
            entity (_type_): entity to update
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int):
        """delete item

        Args:
            item_id (int): identifier

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
