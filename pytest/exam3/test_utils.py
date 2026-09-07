import pytest
from utils import is_even

class TestIsEven:
    def test_even_number(self):
        assert is_even(12) is True

    def test_odd_number(self):
        assert is_even(5) is False

    def test_ziro(self):
        assert is_even(0) is True