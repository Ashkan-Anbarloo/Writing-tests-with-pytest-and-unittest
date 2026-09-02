import pytest

@pytest.fixture
def sample_list():
    return [1 , 2 , 3 , 4 , 5]

@pytest.fixture
def sample_numbers():
    return (10 , 20)