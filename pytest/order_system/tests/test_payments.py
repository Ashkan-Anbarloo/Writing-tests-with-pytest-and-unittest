import pytest
from order_system.payments.getway import process_payment

def test_process_payment_valid():
    result = process_payment(1 , 1000)
    assert result['status'] == 'paid'

def test_process_payment_invalid():
    with pytest.raises(ValueError):
        process_payment(1 , -500)