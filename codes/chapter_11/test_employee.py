from employee import Employee
import pytest
@pytest.fixture
def employee_information():
    employee_information = Employee('shi', 'quan', '5000')
    return employee_information

def test_give_default_raise(employee_information):
    employee_information.give_raise()
    assert employee_information.salary == 10000

def test_give_custom_raise(employee_information):
    employee_information.give_raise('6000')
    assert employee_information.salary == 11000