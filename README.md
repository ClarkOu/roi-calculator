# 人效提升与人力释放测算器 (Streamlit)

A business process automation efficiency estimator for HR and enterprise teams. It helps estimate annual time savings, FTE capacity released, and efficiency improvement for one or multiple process steps.

## Features

- Add multiple process steps and view totals
- Capture assessment metadata (scenario and department)
- Show a detail table (click a row to select)
- Edit (dialog) / delete the selected row
- Export to CSV with summary interpretation row

> Note: Due to limitations of Streamlit's native table components, it's not possible to embed buttons directly inside table cells. The current interaction is: select a row → use the action buttons below.

## How it works (method)

This tool models a process as a list of steps. For each step, you input the baseline workload and the expected efficiency gain after automation. The app then aggregates all steps to estimate:

- Annual time saved (hours/year)
- FTE capacity released (by converting hours to FTE based on your working-hour assumptions)
- Efficiency improvement (before vs after)

Typical workflow:

1) Fill in scenario and department information
2) Add one step per activity in the process
3) Review the table, live metrics, and totals
4) Select a row to edit or delete if assumptions change
5) Export the step list to CSV with summary interpretation for sharing

## Run locally

1) Clone the repo

```bash
git clone https://github.com/ClarkOu/roi-calculator.git
cd roi-calculator
```

2) Create a virtual environment and install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3) Start the app

```bash
streamlit run app.py
```

Open the URL printed in the terminal (usually http://localhost:8501).

## Project structure

- app.py: Streamlit app
- roi_calculator.py: original calculator script (CLI / logic reference)
- requirements.txt: dependencies

## Notes

- CSV export uses UTF-8 with BOM (`utf-8-sig`) so Excel can open it without garbled characters.
