from models.employee import Employee
from reports import PayoutReport


def test_payout_report_generation(capsys):
    employees = [
        Employee(1, "a@a.com", "Test One", "Dev", 160, 50),
        Employee(2, "b@b.com", "Test Two", "QA", 120, 40),
    ]

    report = PayoutReport()
    report.generate(employees)

    captured = capsys.readouterr()
    assert "Test One" in captured.out
    assert "8000.00" in captured.out
    assert "Test Two" in captured.out
    assert "4800.00" in captured.out
    assert "Итого" in captured.out
    assert "12800.00" in captured.out


def test_payout_report_empty(capsys):
    report = PayoutReport()
    report.generate([])

    captured = capsys.readouterr()
    assert "Итого" in captured.out
    assert "0.00" in captured.out
