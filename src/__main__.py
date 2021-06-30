from src.api import TaskService, TaskRepository
from src.shared.models.data import TaskModel
from src.shared.models import Service


def main(api: Service):
    prev_len = len(api.get_all())
    api.create(TaskModel(
        title='test', id=12345, project_id=54321
    ))
    api.delete(12345)
    post_len = len(api.get_all())
    print(prev_len, post_len)


if __name__ == "__main__":
    main(TaskService(TaskRepository()))
