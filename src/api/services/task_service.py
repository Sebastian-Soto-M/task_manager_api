from typing import List

from src.shared.exceptions import (ElementNotFoundException,
                                   InternalErrorException,
                                   IterableNotFoundException)
from src.shared.models import Repository, Service
from src.shared.models.data import TaskModel


class TaskService(Service[int, TaskModel]):

    def __init__(self, repository: Repository[int, TaskModel]):
        super().__init__(repository)

    def get_by_id(self, id: int) -> TaskModel:
        """ Get a task using its unique identification """
        res = self.repository.get_by_id(id)
        if res is not None:
            return res
        else:
            raise ElementNotFoundException(id)

    def get_all(self) -> List[TaskModel]:
        """ Get all tasks available """
        res = self.repository.get_all()
        if res is not None and len(res) > 0:
            return res
        else:
            raise IterableNotFoundException

    def create(self, data: TaskModel) -> bool:
        """ Get all elements available """
        res = self.repository.create(data)
        if res:
            return res
        else:
            raise InternalErrorException(data, 'Failed to create task')

    def update(self, data: TaskModel) -> TaskModel:
        """ Get all elements available """
        obj = self.get_by_id(data.id)
        res = self.repository.update(obj)
        if res is not None:
            return res
        else:
            raise InternalErrorException(data, 'Failed to update task')

    def delete(self, id: int) -> bool:
        """ Get all elements available """
        try:
            self.get_by_id(id)
            return self.repository.delete(id)
        except ElementNotFoundException:

        res =
        if res:
            return res
        else:
            raise InternalErrorException('Failed to delete task')
