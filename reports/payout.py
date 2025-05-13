from typing import List

from models.employee import Employee
from reports.base import BaseReport


class PayoutReport(BaseReport):
    """
    Отчёт по зарплатам.
    """

    def generate(self, employees: List[Employee]) -> None:
        print("\nОтчёт по зарплатам:\n")
        print(f"{'Имя':<25} {'Отдел':<15} {'Часы':<8} {'Ставка':<10} {'Зарплата'}")
        print("-" * 70)

        for emp in employees:
            print(f"{emp.name:<25} {emp.department:<15} {emp.hours_worked:<8.1f} {emp.hourly_rate:<10.2f}"
                  f" {emp.payout():.2f}")

        print("-" * 70)
        total = sum(emp.payout() for emp in employees)
        print(f"{'Итого':<58}{total:.2f}")
