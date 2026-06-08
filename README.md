# 🔍 Automated Data Auditor

A Python-based automation tool for Data Scientists and Analysts to instantly audit CSV datasets for quality issues.

## 🌟 Features
- **Automated Summary:** Generates row and column counts instantly.
- **Quality Check:** Detects missing values (NaN) across the entire dataset.
- **Logical Duplicate Detection:** Identifies duplicate entries based on specific identity columns (e.g., Name).
- **Type Inspection:** Reports data types to identify potential conversion issues.
- **Auto-Export:** Saves every audit as a `.txt` report in the `/reports` folder.

## 🛠️ Tech Stack
- **Language:** Python 3.10
- **Library:** Pandas (Data manipulation)
- **Environment:** Conda

## 📁 Project Structure
- `scripts/`: Contains the main auditing logic (`auditor.py`).
- `data/`: Sample datasets for testing.
- `reports/`: Automatically generated audit summaries.

## 🚀 How to Run
1. Activate your environment: `conda activate auditor_env`
2. Run the script: `python scripts/auditor.py`
3. Check the `reports/` folder for your results.

---
**Author:** Muhammad Usman  
*Building a professional Data Science portfolio step-by-step.*