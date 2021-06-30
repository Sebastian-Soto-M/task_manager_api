from typing import Dict, List
from unittest import TestCase

from .repositories import TestTaskRepository

API_TESTS: Dict[str, List[TestCase]] = {
    'repositories': [TestTaskRepository],
    'controllers': [],
    'services': [],
}
