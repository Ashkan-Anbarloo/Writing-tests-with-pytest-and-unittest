import pytest
import app
import datetime


def fake_get(url):
    class FakeResponse:
        def json(self):
            return{
                'rates':{
                    'IRR':5000000
                }
            }
    return FakeResponse()

def test_get_usd_price(monkeypatch):
    monkeypatch.setattr('app.requests.get', fake_get)

    result = app.get_usd_price()
    assert result == 5000000


def fake_now():
    return datetime.datetime(2024 , 1 , 1 , 8 , 30)

def test_is_morning(monkeypatch):
    monkeypatch.setattr('app.datetime.datetime', type('MockDateTime', (), {'now':staticmethod(fake_now)}))
    assert app.is_morning() is True