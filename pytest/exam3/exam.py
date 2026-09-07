import pytest

def get_name(user_id):
    if user_id == 1:
        return "ali"
    raise ValueError('User not found')

class TestGetName:
    @pytest.fixture
    def valid_user_id(self):
        return 1

    def test_valid_user_id(self, valid_user_id):
        assert get_name(valid_user_id) == 'ali'

    def test_invalid_user_id(self):
        with pytest.raises(ValueError):
            get_name(5)