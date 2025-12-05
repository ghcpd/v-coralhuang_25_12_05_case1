from generate_data import write_all, generate_students
from process_admissions import load_data, validate_and_clean, attach_choices_and_evaluate, export_final
from pathlib import Path
import pandas as pd

def test_full_processing_pipeline(tmp_path):
    out = tmp_path / 'admissions.xlsx'
    write_all(output_file=out)
    students, choices, programs = load_data(out)
    students = validate_and_clean(students)
    assert 'Aggregate' in students.columns
    df = attach_choices_and_evaluate(students, choices, programs)
    assert 'AssignedChoice' in df.columns
    assert set(['FirstChoice','SecondChoice','ThirdChoice']).issubset(df.columns)
    # Ensure SuggestedProgram exists and is non-empty
    assert df['SuggestedProgram'].notnull().all()
    # Export final
    final_file = tmp_path / 'final.xlsx'
    export_final(df, final_file)
    assert final_file.exists()
    xls = pd.ExcelFile(final_file)
    assert 'final' in xls.sheet_names
