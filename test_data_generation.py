import pandas as pd
from generate_data import write_all, generate_students
from pathlib import Path

def test_generate_students_count_and_id():
    df = generate_students(n=60)
    assert len(df) == 60
    assert df['StudentID'].iloc[0].startswith('UG2025')
    assert df['StudentID'].str.match(r'^UG2025\d{4}$').all()


def test_write_all_creates_file(tmp_path):
    out = tmp_path / 'test_admissions.xlsx'
    # call write_all to write to tmp path
    from generate_data import write_all
    write_all(output_file=out)
    assert out.exists()
    xls = pd.ExcelFile(out)
    assert set(xls.sheet_names) == {'students','choices','programs'}
    students = pd.read_excel(out, sheet_name='students')
    assert len(students) >= 50
