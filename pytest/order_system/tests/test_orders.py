import pytest
from order_system.orders.services import create_order

def test_create_order_valid():
    result = create_order(1,2)
    assert result['status'] == 'created'


def test_create_order_invalid():
    with pytest.raises(ValueError):
        create_order(None,2)