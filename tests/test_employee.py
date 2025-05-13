import pytest

from models.employee import Employee


def test_employee_creation():
    data = {
        'id': '1',
        'email': 'alice@example.com',
        'name': 'Alice Johnson',
        'department': 'Marketing',
        'hours_worked': '160',
        'hourly_rate': '50'
    }

    employee = Employee.from_dict(data)

    assert employee.id == 1
    assert employee.email == 'alice@example.com'
    assert employee.name == 'Alice Johnson'
    assert employee.department == 'Marketing'
    assert employee.hours_worked == 160
    assert employee.hourly_rate == 50
    assert employee.payout() == 160 * 50


def test_employee_salary_calculation():
    data = {
        'id': '2',
        'email': 'bob@example.com',
        'name': 'Bob Smith',
        'department': 'Design',
        'hours_worked': '150',
        'hourly_rate': '40'
    }

    employee = Employee.from_dict(data)
    assert employee.payout() == 150 * 40


def test_employee_with_rate_key():
    data = {
        'id': '3',
        'email': 'carol@example.com',
        'name': 'Carol Davis',
        'department': 'Engineering',
        'hours_worked': '170',
        'rate': '60'
    }
    employee = Employee.from_dict(data)
    assert employee.hourly_rate == 60
    assert employee.payout() == 170 * 60


def test_employee_with_salary_key():
    data = {
        'id': '4',
        'email': 'dan@example.com',
        'name': 'Dan Lee',
        'department': 'Sales',
        'hours_worked': '140',
        'salary': '45'
    }
    employee = Employee.from_dict(data)
    assert employee.hourly_rate == 45
    assert employee.payout() == 140 * 45


def test_employee_invalid_hours():
    data = {
        'id': '6',
        'email': 'frank@example.com',
        'name': 'Frank Wood',
        'department': 'Support',
        'hours_worked': 'abc',
        'hourly_rate': '30'
    }
    with pytest.raises(ValueError, match="Некорректные данные сотрудника"):
        Employee.from_dict(data)
