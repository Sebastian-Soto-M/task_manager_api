# type: ignore
from abc import ABC, abstractmethod
from typing import List

from ..interfaces import ID, OBJ, ICrud


class Repository(ICrud[ID, OBJ], ABC):
    @abstractmethod
    def configure(self):
        """
        Here is where the Repository's credentials, authentication and
        other procedures are executed
        """

class Service(ICrud[ID, OBJ], ABC):
    def __init__(self, repository: Repository[ID, OBJ]):
        self.__repository = repository
        self.__repository.configure()

    @property
    def repository(self):
        return self.__repository

    def get_by_id(self, id: ID) -> OBJ:
        """ Get an element using its unique identification """
        raise NotImplementedError

    def get_all(self) -> List[OBJ]:
        """ Get all elements available """
        raise NotImplementedError

    def create(self, data: OBJ) -> bool:
        """ Get all elements available """
        raise NotImplementedError

    def update(self, data: OBJ) -> OBJ:
        """ Get all elements available """
        raise NotImplementedError

    def delete(self, id: ID) -> bool:
        """ Get all elements available """
        raise NotImplementedError
