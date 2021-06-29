from pathlib import Path
from os.path import join


def get_data_file(name: str):
    return Path(join(Path(__file__).parent.parent.parent,
                'data', f'{name}.json'))
