from src.shared.interfaces import ICrud
from src.shared.models import TaskModel, Service, Repository
from typing import Optional, List


class TaskService(Service[int, TaskModel]):

    def __init__(self, repository: Repository):
        super().__init__(repository)

    def get_by_id(self, id: int) -> Optional[TaskModel]:
        """ Get an element using its unique identification """
        return self.repository.get_by_id(id)

    def get_all(self) -> Optional[List[TaskModel]]:
        """ Get all elements available """
        return self.repository.get_all()

    def create(self, data: TaskModel) -> bool:
        """ Get all elements available """
        return self.repository.create(data)

    def update(self, data: TaskModel) -> Optional[TaskModel]:
        """ Get all elements available """
        return self.repository.update(data)

    def delete(self, id: int) -> bool:
        """ Get all elements available """
        return self.repository.delete(id)
