# UG Admission Checker (WASSCE) - Final Solution

This workspace contains a Jupyter Notebook solution which implements an admission-check procedure for WASSCE applicants against program cutoffs.

What you'll find here:
- `UG_admission_wassce_solution.ipynb` — final notebook that reads input Excel sheets, applies admission logic using if/elif statements, and writes a beautified Excel report.
- `students_wassce.xlsx` — generated sample students (60 students) with WASSCE aggregates.
- `choices.xlsx` — each student's first/second/third choices.
- `programs_cutoffs.xlsx` — program list and cutoff aggregates.
- Output files produced when running the notebook / scripts:
  - `admission_results.xlsx`
  - `students_results_with_recommendations.xlsx`
  - `final_admission_output.xlsx` (beautified workbook with conditional formatting and a summary sheet)

How to run:
1. Create and activate a Python 3 environment (the project's `.venv` is present if you've used the workspace tools).
2. Install dependencies: `pip install -r requirements.txt`.
3. Open and run `UG_admission_wassce_solution.ipynb` in Jupyter; or run the notebook cells in order. The final files will be generated in the workspace folder.

Notes:
- Student IDs follow the `UG2025xxxx` format as required.
- The logic follows if -> elif -> elif when checking First, Second, and Third choices.
- The code suggests other programs that match the student's aggregate or close near-misses for fee-paying options.

Good luck and feel free to adapt the datasets and cutoffs for your institution!
