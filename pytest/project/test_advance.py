import pytest
from app import fetch_data_from_api , heavy_processing

@pytest.mark.api
def test_fetch_data_from_api():
    result = fetch_data_from_api()
    assert result['status'] == 'ok'

@pytest.mark.slow
def test_heavy_processing():
    result = heavy_processing()
    assert result > 0