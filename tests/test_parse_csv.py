import tempfile
from parsers.csv_parser import parse_csv


def test_parse_csv_with_varied_header_names():
    content = """id,email,name,department,hours_worked,salary
1,test@example.com,Test User,Engineering,100,25
"""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write(content)
        tmp.seek(0)
        rows = parse_csv(tmp.name)

    assert len(rows) == 1
    assert rows[0]["salary"] == "25"
