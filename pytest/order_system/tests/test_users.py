import pytest
from order_system.users.models import get_user

def test_get_existing_user():
    user = get_user(1)
    assert user['name'] == 'ali'

def test_get_non_existing_user():
    with pytest.raises(LookupError):
        get_user(10)