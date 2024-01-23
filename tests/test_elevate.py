from unittest.mock import patch
import elevator.elevate


@patch('elevator.elevate.input', side_effect=[
    'test',
    'andy'
])
def test_get_model_data(mock_inputs):
    assert elevator.elevate.get_model_data() == {
        'model_name': 'test',
        'author': 'andy'
    }


def test_get_model_data_bad():
    pass


def test_save_model_data():
    pass


def test_load_model_data():
    pass


def test_run():
    pass


def test_run_bad():
    pass
