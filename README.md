# ROI Calculator (Streamlit)

A business process automation ROI estimator. It helps estimate annual time savings, FTE capacity released, and efficiency improvement for one or multiple process steps.

## Features

- Add multiple process steps and view totals
- Show a detail table (click a row to select)
- Edit (dialog) / delete the selected row
- Export to CSV

> Note: Due to limitations of Streamlit's native table components, it's not possible to embed buttons directly inside table cells. The current interaction is: select a row → use the action buttons below.

## How it works (method)

This tool models a process as a list of steps. For each step, you input the baseline workload and the expected efficiency gain after automation. The app then aggregates all steps to estimate:

- Annual time saved (hours/year)
- FTE capacity released (by converting hours to FTE based on your working-hour assumptions)
- Efficiency improvement (before vs after)

Typical workflow:

1) Add one step per activity in the process
2) Review the table and totals
3) Select a row to edit or delete if the assumptions change
4) Export the step list to CSV for sharing

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
