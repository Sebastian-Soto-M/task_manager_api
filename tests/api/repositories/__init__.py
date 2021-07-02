from unittest import TestCase

from src.api import TaskRepository
from src.shared.models import Repository
from src.shared.models.data import TaskModel


class TestTaskRepository(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repository: Repository[int, TaskModel] = TaskRepository()
        cls.repository.configure()

    def tearDown(self):
        self.repository.configure()

    def test_get_by_id(self):
        obj = self.repository.get_by_id(555)
        self.assertIsNotNone(obj)
        if obj is not None:
            self.assertEqual(obj.title, "Metoprolol succinate")

    def test_get_all(self):
        lst = self.repository.get_all()
        self.assertIsNotNone(lst)
        if lst is not None:
            self.assertGreater(len(lst), 20)
