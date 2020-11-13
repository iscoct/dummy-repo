from unittest.mock import patch
import pytest

@patch('src.main.dummy_sum', return_value=0)
def test_dummy(dummy_sum_mock):
    from src.main import result

    assert result == 2

    # Si ejecutas pytest -s
    # Verás que muestra Dummy sum como la función verdadera