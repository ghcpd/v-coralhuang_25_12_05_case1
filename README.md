# Admissions Matching Notebook

Files:
- `admissions.ipynb` — Jupyter Notebook with code to create sample applicants and evaluate admissions.
- `requirements.txt` — Python package dependencies.

Quick start (PowerShell):

1. Create and activate a virtual environment (optional but recommended):

   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

3. Open the notebook in Jupyter (or run `admissions.ipynb` interactively):

   jupyter notebook admissions.ipynb

Outputs:
- `applicants_input.xlsx` contains the three input sheets: Students, Choices, Programs.
- `admissions_results.xlsx` contains the Results sheet plus a Summary sheet and chart.

If pandas isn't available in your Python environment, please install the packages using pip as shown above.

Note: This repository provides a teaching example. Adjust cutoffs and logic to match local admissions policies.
