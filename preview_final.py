import pandas as pd

df = pd.read_excel('admissions_result.xlsx', sheet_name='final')
print('Columns:', df.columns.tolist())
print(df[['StudentID','AssignedChoice','FirstChoice','SecondChoice','ThirdChoice','SuggestedProgram']].head().to_string(index=False))
