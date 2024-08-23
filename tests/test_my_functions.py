import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(78, 23)
    assert result == 101


def test_add_strings():
    result = my_functions.add("i like ", "pizza")
    assert result == "i like pizza"


def test_divide():
    result = my_functions.divide(75, 3)
    assert result == 25


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)
    
