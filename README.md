# Workforce Efficiency & FTE Release Estimator (Streamlit)

[中文](README.zh.md)

An automation efficiency estimator for HR and enterprise teams. It helps estimate annual time savings, FTE capacity released, and efficiency improvement across one or multiple process steps.

## Features

- Add multiple process steps and view totals
- Capture assessment metadata (scenario and department)
- Show a detailed table (select one row at a time)
- Edit (dialog) / delete the selected row
- Export to CSV with a summary interpretation row

> Note: Due to Streamlit table limitations, action buttons cannot be embedded directly in cells. Current interaction: select a row → use the action buttons below.

## How It Works

This tool models a process as a list of steps. For each step, you enter baseline workload and expected post-automation efficiency. The app then aggregates all steps to estimate:

- Annual time saved (hours/year)
- FTE capacity released (hours converted to FTE based on working-hour assumptions)
- Efficiency improvement (before vs. after)

Typical workflow:

1) Fill in scenario and department information
2) Add one step per process activity
3) Review the table, live metrics, and totals
4) Select a row to edit or delete when assumptions change
5) Export CSV with summary interpretation for sharing

## Run Locally

1) Clone the repository

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

## Project Structure

- app.py: Streamlit app
- roi_calculator.py: original calculator script (CLI / logic reference)
- requirements.txt: dependencies

## Notes

- CSV export uses UTF-8 with BOM (`utf-8-sig`) so Excel opens it without garbled characters.
