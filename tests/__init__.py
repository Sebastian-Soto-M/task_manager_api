import logging
import sys
from itertools import chain
from typing import Dict, List
from unittest import TestCase

from tests.api import API_TESTS
from tests.utils import cli_options

TESTS: Dict[str, List[TestCase]] = {
    'api': list(chain.from_iterable(API_TESTS.values())),
    'api-controllers': API_TESTS['controllers'],
    'api-repositories': API_TESTS['repositories'],
    'api-services': API_TESTS['services'],
    'shared': [],
}


CLI_OPTS = cli_options(TESTS.keys())

logging_mode = logging.INFO if not CLI_OPTS.verbose else logging.DEBUG
logging.basicConfig(level=logging_mode, stream=sys.stdout,
                    format='%(levelname)s\t%(message)s')
