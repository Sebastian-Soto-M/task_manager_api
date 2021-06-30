import logging
from typing import List
from unittest import TestCase, TestSuite, TextTestRunner, makeSuite

from . import CLI_OPTS, TESTS

logger = logging.getLogger('TestMain')


def add_test_case_list_to_suite(suite: TestSuite, test_cases: List[TestCase]):
    for case in test_cases:
        suite.addTest(makeSuite(case))


def get_suite() -> TestSuite:
    suite = TestSuite()
    selected_suite = CLI_OPTS.suite
    if selected_suite != False:
        add_test_case_list_to_suite(suite, TESTS[selected_suite])
    else:
        tests = set()
        for k, v in TESTS.items():
            title = k.replace('-', ' ').capitalize()
            tests.add(f'Testing:\t{title}')
            add_test_case_list_to_suite(suite, v)
        logger.info(f'The following tests will run: {tests}')
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(get_suite())
