from src.shared.models import TaskModel, Service, Repository
from src.shared.utils import get_data_file
import json
from typing import Dict, Tuple, Optional, List


def parse_task(data: dict) -> Tuple[int, TaskModel]:
    task = TaskModel(**data)
    return (task.id, task)


class TaskRepository(Repository[int, TaskModel]):
    def __init__(self):
        self.__data: Dict[int, TaskModel] = dict()

    def configure(self):
        tmp_data = json.load(get_data_file('tasks').open('r'))
        for obj in tmp_data:
            obj = TaskModel(**obj)
            self.__data[obj.id] = obj

    def get_by_id(self, id: int) -> Optional[TaskModel]:
        """ Get an element using its unique identification """
        return self.__data.get(id)

    def get_all(self) -> Optional[List[TaskModel]]:
        """ Get all elements available """
        return [obj for obj in self.__data.values()]

    def create(self, data: TaskModel) -> bool:
        """ Get all elements available """
        self.__data[data.id] = data
        return True

    def update(self, data: TaskModel) -> Optional[TaskModel]:
        """ Get all elements available """
        return self.__data.get(data.id)

    def delete(self, id: int) -> bool:
        """ Get all elements available """
        self.__data.pop(id)
        return True
