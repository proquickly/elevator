import pytest
from unittest.mock import patch
import elevator.elevate


@patch('elevator.elevate.input', side_effect=[
    'test',
    'andy',
    10,
    100,
    600
])
def test_get_model_data(mock_inputs):
    assert elevator.elevate.get_model_data() == {
        'model_name': 'test',
        'author': 'andy',
        'floors': 10,
        'width': 100.0,
        'length': 600.0,
    }


@patch('elevator.elevate.input', side_effect=[
    'test',
    'andy',
    'a',
    100,
    600
])
def test_get_model_data_bad(mock_inputs):
    with pytest.raises(ValueError):
        assert elevator.elevate.get_model_data() is None


def test_save_model_data():
    pass


def test_load_model_data():
    pass


def test_run():
    pass


def test_run_bad():
    pass
