from typing import List, Dict


def parse_csv(filepath: str) -> List[Dict[str, str]]:
    """
    Читает CSV-файл и возвращает список строк как словарей с данными.
    Не использует стандартные библиотеки `csv` или `pandas`.
    """
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        return []

    headers = [h.strip() for h in lines[0].strip().split(",")]
    rows = []

    for line in lines[1:]:
        values = [v.strip() for v in line.strip().split(",")]
        if len(values) != len(headers):
            raise ValueError(f"Неверное количество столбцов в строке: {line}")
        row = dict(zip(headers, values))
        rows.append(row)

    return rows
