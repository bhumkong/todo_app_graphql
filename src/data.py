from src.models import Data

_data = Data(
    todos=[],
    users=[],
)


def get_data():
    return _data


def save_data():
    with open('data.json', 'w') as f:
        f.write(_data.model_dump_json(indent=2))


def load_data():
    global _data
    with open('data.json', 'r') as f:
        _data = Data.model_validate_json(f.read())
