from app import add


def test_add(sample_numbers):
    a , b = sample_numbers
    assert add(a,b) == 30