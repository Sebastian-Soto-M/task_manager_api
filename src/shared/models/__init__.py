from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, TypeVar

from ..interfaces import ID, OBJ, ICrud
from .data import TaskModel


class Repository(ICrud[ID, OBJ], ABC):
    @abstractmethod
    def configure(self):
        """
        Here is where the Repository's credentials, authentication and
        other procedures are executed
        """


class Service(ICrud[ID, OBJ], ABC):
    def __init__(self, repository: Repository):
        self.__repository = repository
        self.__repository.configure()

    @property
    def repository(self):
        return self.__repository

    def get_by_id(self, id: ID) -> Optional[OBJ]:
        """ Get an element using its unique identification """
        return self.repository.get_by_id(id)

    def get_all(self) -> Optional[List[OBJ]]:
        """ Get all elements available """
        return self.repository.get_all(id)

    def create(self, data: OBJ) -> bool:
        """ Get all elements available """
        return self.repository.create(data)

    def update(self, data: OBJ) -> Optional[OBJ]:
        """ Get all elements available """
        return self.repository.update(data)

    def delete(self, id: ID) -> bool:
        """ Get all elements available """
        return self.repository.delete(id)
