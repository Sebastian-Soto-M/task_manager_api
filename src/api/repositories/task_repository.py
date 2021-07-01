import json
from typing import Dict, List, Optional, Tuple

from src.shared.models import Repository, Service, TaskModel
from src.shared.utils import get_data_file


class TaskRepository(Repository[int, TaskModel]):
    def __init__(self):
        self.__data: Dict[int, TaskModel] = dict()

    def configure(self):
        with get_data_file('tasks').open('r') as file:
            tmp_data = json.load(file)
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
