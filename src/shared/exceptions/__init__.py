from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from src.shared.enums import DefaultExceptionMessages


@dataclass
class ExceptionResult:
    msg: str
    obj: Any


class CustomException(Exception, ABC):
    def __init__(self):
        super().__init__(repr(self.get_result()))

    @abstractmethod
    def get_result(self) -> ExceptionResult:
        """
        This method returns the information needed for the user to
        know what went wrong
        """


class IterableNotFoundException(CustomException):
    def get_result(self) -> ExceptionResult:
        return ExceptionResult(
            msg=DefaultExceptionMessages.ITERABLE_NOT_FOUND.value,
            obj=list()
        )


class ElementNotFoundException(CustomException):

    def __init__(self, id: Any):
        self.id = id

    def get_result(self) -> ExceptionResult:
        return ExceptionResult(msg=DefaultExceptionMessages.ELEMENT_NOT_FOUND.value,
                               obj=self.id)


class InternalErrorException(CustomException):
    def __init__(self, obj: Any, msg: str):
        self.obj = obj
        self.msg = msg

    def get_result(self) -> ExceptionResult:
        return ExceptionResult(msg=self.msg, obj=self.obj)
