from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

ID = TypeVar('ID')
OBJ = TypeVar('OBJ')


class ICrud(Generic[ID, OBJ], ABC):
    @abstractmethod
    def get_by_id(self, id: ID) -> Optional[OBJ]:
        """ Get an element using its unique identification """
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Optional[List[OBJ]]:
        """ Get all elements available """
        raise NotImplementedError

    @abstractmethod
    def create(self, data: OBJ) -> bool:
        """ Get all elements available """
        raise NotImplementedError

    @abstractmethod
    def update(self, data: OBJ) -> Optional[OBJ]:
        """ Get all elements available """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: ID) -> bool:
        """ Get all elements available """
        raise NotImplementedError
