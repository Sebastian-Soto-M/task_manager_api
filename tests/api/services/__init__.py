
from unittest import TestCase, main, skip

from src.api import TaskRepository, TaskService
from src.shared.models import Repository, Service
from src.shared.models.data import TaskModel


class TestTaskService(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service: Service = TaskService(TaskRepository())

    def tearDown(self):
        self.service.repository.configure()

    def test_get_by_id(self):
        obj: TaskModel = self.service.get_by_id(5943367)
        self.assertEqual(obj.title, "et consectetur sunt")
