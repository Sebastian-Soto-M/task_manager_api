from typing import Any

from src.api import TaskRepository, TaskService
from src.shared.models import Service
from src.shared.models.data import TaskModel


def main(api: Service[Any, Any]):
    prev_len = len(api.get_all())
    api.create(TaskModel(
        title='test', id=12345, project_id=54321
    ))
    print(api.get_by_id(12345).json())
    api.delete(12345)
    post_len = len(api.get_all())
    print(prev_len, post_len)


if __name__ == "__main__":
    main(TaskService(TaskRepository()))
