from src.api import TaskService, TaskRepository
from src.shared.interfaces import ICrud


def main(api: ICrud):
    print(api.get_by_id(5943367))


if __name__ == "__main__":
    main(TaskService(TaskRepository()))
