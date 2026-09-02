from app import double , add , apply_discount , multiply
import pytest




# def test_double():
#     assert double(1) == 2

@pytest.mark.parametrize('input_value , expected_output' , [
    (2,4),
    (5,10),
    (-3,-6),
    (0,0),
    (1.5,3.0),
])

def test_double(input_value, expected_output):
    assert double(input_value) == expected_output


@pytest.mark.parametrize('x,y,expected' , [
    (1,2,3),
    (0,0,0),
    (-1,5,4),
    (2.5,3.5,6),
])
def test_add(x,y,expected):
    assert add(x,y) == expected


@pytest.fixture
def base_price():
    return 100

@pytest.mark.parametrize('discount_percent,expected' , [
    (10,90),
    (0,100),
    (50,50),
    (100,0),
])
def test_apply_discount(base_price,discount_percent,expected):
    assert apply_discount(base_price,discount_percent) == expected


@pytest.mark.parametrize('a , b , expected' , [
    (2,3,6),
    (0,100,0),
    (-1,5,-5),
])
class TestMultiply:
    def test_result(self , a , b, expected):
        assert multiply(a,b) == expected

    def test_type(self ,a ,b ,expected):
        result = multiply(a,b)
        assert isinstance(result,(int,float))


@pytest.mark.parametrize('a , b , expected' , [
    (2,3,6),
    (0,100,0),
    (-1,5,-5),
],ids=['positive' , 'zero' , 'negative'])
def test_multiplay_name(a , b , expected):
    assert multiply(a,b) == expected