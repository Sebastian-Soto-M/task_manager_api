import json
from typing import Dict, List, Optional

from src.shared.models import Repository
from src.shared.models.data import TaskModel
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
        """ Get an element by id """
        return self.__data.get(id)

    def get_all(self) -> Optional[List[TaskModel]]:
        """ Get all elements available """
        return [obj for obj in self.__data.values()]

    def create(self, data: TaskModel) -> bool:
        """ Create element by id """
        try:
            self.__data[data.id] = data
            return True
        except KeyError:
            return False

    def update(self, data: TaskModel) -> Optional[TaskModel]:
        """ Update element by id """
        self.__data[data.id] = data
        try:
            self.__data[data.id] = data
            return data
        except KeyError:
            return None

    def delete(self, id: int) -> bool:
        """ Delete element by id """
        try:
            self.__data.pop(id)
            return True
        except KeyError:
            return False

    def clear(self):
        self.__data.clear()
