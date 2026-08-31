import pytest
from app import double
import os

@pytest.fixture
def sample_number():
    return 5

def test_double_positive(sample_number):
    assert double(sample_number) == 10

def test_double_negative(sample_number):
    assert double(sample_number) == -10

def test_double_is_even(sample_number):
    assert double(sample_number) % 2 == 0

@pytest.fixture
def temp_file():
    fileName = 'temp.txt'
    with open(fileName , 'w') as f:
        f.write('hello pytest')
    yield fileName
    os.remove(fileName)

def test_temp_file_is_empty(temp_file):
    assert temp_file == 'temp.txt'