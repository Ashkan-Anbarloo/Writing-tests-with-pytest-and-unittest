from app import divide , InvalidAgeError , register_user
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)

def test_divide_by_zero_message():
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(5,0)

    assert 'division by zero' in str(exc_info.value)


def test_invalidd_age():
    with pytest.raises(InvalidAgeError) as e:
        register_user(-5)
    assert 'منفی' in str(e.value)


@pytest.mark.parametrize('age' , [-1,-10,-100])
def test_multiply_invalid_ages(age):
    with pytest.raises(InvalidAgeError):
        register_user(age)