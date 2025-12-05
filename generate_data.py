import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path(__file__).parent

def generate_students(n=60, seed=42) -> pd.DataFrame:
    np.random.seed(seed)
    ids = [f"UG2025{str(i).zfill(4)}" for i in range(1, n+1)]
    first_names = np.random.choice(['Akosua','Kwame','Efua','Kofi','Ama','Yaw','Adjoa','Kojo','Esi','Nana'], size=n)
    last_names = np.random.choice(['Mensah','Ofori','Acheampong','Boateng','Asante','Duku','Agyapong','Antwi'], size=n)
    names = [f"{fn} {ln}" for fn, ln in zip(first_names, last_names)]
    # Generate 6 subject scores between 4 and 20 (WASSCE-like scaled for example)
    subjects = ['Eng','Math','Sci','Soc','Rel','Elec']
    scores = {s: np.random.randint(4,21,size=n) for s in subjects}
    df = pd.DataFrame({'StudentID': ids, 'Name': names})
    for s in subjects:
        df[s] = scores[s]
    # aggregate lower is better in many Ghanaian systems; here we'll sum and lower is better
    df['Aggregate'] = df[subjects].sum(axis=1)
    return df


def generate_choices(students_df: pd.DataFrame) -> pd.DataFrame:
    programs = ['Computer Science','Business Administration','Psychology','Law','Medicine','Nursing','Economics','Engineering']
    n = len(students_df)
    np.random.seed(123)
    # Each student selects 3 distinct choices
    choices = [np.random.choice(programs, size=3, replace=False).tolist() for _ in range(n)]
    df = pd.DataFrame({
        'StudentID': students_df['StudentID'],
        'Choice1': [c[0] for c in choices],
        'Choice2': [c[1] for c in choices],
        'Choice3': [c[2] for c in choices]
    })
    return df


def generate_programs() -> pd.DataFrame:
    data = [
        ('Computer Science', 60),
        ('Engineering', 58),
        ('Medicine', 55),
        ('Law', 50),
        ('Economics', 52),
        ('Business Administration', 48),
        ('Psychology', 50),
        ('Nursing', 62),
    ]
    df = pd.DataFrame(data, columns=['Program','Cutoff'])
    return df


def write_all(output_file: Path = DATA_PATH / 'admissions_data.xlsx') -> Path:
    students = generate_students()
    choices = generate_choices(students)
    programs = generate_programs()
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        students.to_excel(writer, sheet_name='students', index=False)
        choices.to_excel(writer, sheet_name='choices', index=False)
        programs.to_excel(writer, sheet_name='programs', index=False)
    return output_file

if __name__ == '__main__':
    out = write_all()
    print('Wrote data to', out)
