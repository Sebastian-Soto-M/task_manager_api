from typing import Optional
from unittest import TestCase

from src.api import TaskRepository, TaskService
from src.shared.enums import DefaultExceptionMessages
from src.shared.exceptions import ElementNotFoundException, ExceptionResult
from src.shared.models import Service
from src.shared.models.data import TaskModel


class TestTaskService(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service: Service[int, TaskModel] = TaskService(TaskRepository())

    def tearDown(self):
        self.service.repository.configure()

    def test_get_by_id_invalid(self):
        id = 1239393
        expected = ExceptionResult(
            obj=id, msg=DefaultExceptionMessages.ELEMENT_NOT_FOUND.value)
        with self.assertRaises(ElementNotFoundException) as context:
            self.service.get_by_id(id)
        self.assertEqual(context.exception.get_result(), expected)

    def test_get_by_id_valid(self):
        obj: Optional[TaskModel] = self.service.get_by_id(555)
        self.assertIsNotNone(obj)

    def test_get_all_invalid(self):
        data = self.service.get_all()
        self.assertIsInstance(data, list)
        if data is not None:
            self.assertGreater(len(data), 3)

    def test_get_all_valid(self):
        repo: TaskRepository = self.service.repository
        repo.clear()
        data = self.service.get_all()
        self.assertIsInstance(data, list)
        if data is not None:
            self.assertGreater(len(data), 3)

    def test_create(self):
        pass
