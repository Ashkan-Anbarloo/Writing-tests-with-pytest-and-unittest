import pytest

@pytest.fixture(scope='session')
def session_resource():
    print('\n[setup] Session-level fixture')
    yield 'session'
    print('\n[teardown] Session-level fixture')

@pytest.fixture(scope='module')
def module_resource():
    print('\n[setup] Module-level fixture')
    yield 'module'
    print('\n[teardown] Module-level fixture')

@pytest.fixture(scope='class')
def class_resource():
    print('\n[setup] Class-level fixture')
    yield 'class'
    print('\n[teardown] Class-level fixture')

@pytest.fixture(scope='function')
def function_resource():
    print('\n[setup] Function-level fixture')
    yield 'function'
    print('\n[teardown] Function-level fixture')

def test_first(function_resource, module_resource , session_resource):
    print('Running test_first')
    assert function_resource == 'function'
    assert module_resource == 'module'
    assert session_resource == 'session'

def test_secend(function_resource, module_resource , session_resource):
    print('Running test_secend')
    assert function_resource == 'function'
    assert module_resource == 'module'
    assert session_resource == 'session'

class TestClass:
    def test_in_class_1(self , function_resource , class_resource):
        print('Running test_in_class_1')
        assert class_resource == 'class'

    def test_in_class_2(self , function_resource , class_resource):
        print('Running test_in_class_2')
        assert class_resource == 'class'