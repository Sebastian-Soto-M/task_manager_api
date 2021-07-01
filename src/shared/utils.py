from os.path import join
from pathlib import Path


def get_data_file(name: str):
    return Path(join(Path(__file__).parent.parent.parent,
                'data', f'{name}.json'))
