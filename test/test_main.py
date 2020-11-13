from unittest.mock import patch
import pytest

from src.main import result

@patch('src.main.dummy_sum', return_value=0)
def test_dummy(dummy_sum_mock):
    assert result == 2

    # A mi me gustaría que fuera result == 0
    # Esto que parece una tontería, para ciertas cosas tiene grandes implicaciones
    # yo quiero sustituir (mockear) dummy_sum y que ni siquiera procese el módulo dummy