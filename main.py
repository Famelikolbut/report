import argparse
import sys

from models.employee import Employee
from parsers.csv_parser import parse_csv
from reports import REPORTS


def parse_args():
    parser = argparse.ArgumentParser(description="Скрипт формирования отчётов по зарплате.")
    parser.add_argument("files", nargs="*", help="Пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="Название отчёта, например: payout")
    return parser.parse_args()


def main():
    args = parse_args()

    if not args.files:
        print("❌ Не указаны входные CSV-файлы.")
        sys.exit(1)

    report_type = args.report
    if report_type not in REPORTS:
        print(f"❌ Отчёт '{report_type}' не найден.")
        print(f"✅ Доступные отчёты: {', '.join(REPORTS.keys())}")
        sys.exit(1)

    report_class = REPORTS[report_type]
    all_employees = []

    for file_path in args.files:
        try:
            rows = parse_csv(file_path)
            employees = [Employee.from_dict(row) for row in rows]
            all_employees.extend(employees)
        except Exception as e:
            print(f"❌ Ошибка при обработке файла {file_path}: {e}")
            sys.exit(1)

    try:
        report = report_class()
        report.generate(all_employees)
    except Exception as e:
        print(f"❌ Ошибка при генерации отчёта: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
