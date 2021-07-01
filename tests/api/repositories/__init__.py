from unittest import TestCase, main, skip

from src.api import TaskRepository, TaskService
from src.shared.models import Repository, Service
from src.shared.models.data import TaskModel


class TestTaskRepository(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repository: Repository = TaskRepository()
        cls.repository.configure()

    def tearDown(self):
        self.repository.configure()

    def test_get_by_id(self):
        obj: TaskModel = self.repository.get_by_id(5943367)
        self.assertEqual(obj.title, "et consectetur sunt")
