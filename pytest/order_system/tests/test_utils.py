from order_system.utils.helpers import format_price , is_valid_id
import pytest

def test_format_price():
    assert format_price(1000000) == '1000000 تومان '

def test_is_valid_id():
    assert is_valid_id(50) is True

def test_invalid_str():
    assert is_valid_id('reza') is False

def test_invalid_negative():
    assert is_valid_id(-1) is False