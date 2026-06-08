import pandas as pd
import os

def run_audit(file_path):
    # This line tells the computer to start looking at our file
    print(f"--- Starting Audit for: {file_path} ---")
    
    # 1. Load the data using Pandas
    df = pd.read_csv(file_path)
    
    # 2. Count rows and columns
    row_count = len(df)
    col_count = len(df.columns)
    
    # 3. Check for "Empty" (Missing) cells
    missing_values = df.isnull().sum().sum()
    
    # Check for duplicates specifically in the 'name' column
    duplicate_count = df.duplicated(subset=['name']).sum()
    
    # 5. Build a text report
    report = f"""
    DATA QUALITY AUDIT REPORT
    =========================
    File Analyzed: {file_path}
    Total Rows: {row_count}
    Total Columns: {col_count}
    
    ISSUES FOUND:
    - Missing Values: {missing_values}
    - Duplicate Rows: {duplicate_count}
    
    COLUMN DATA TYPES:
    {df.dtypes}
    """
    
    # Print the report to the screen
    print(report)
    
    # 6. Save the report to the 'reports' folder
    output_file = "reports/audit_summary.txt"
    with open(output_file, "w") as f:
        f.write(report)
    
    print(f"✅ Audit Complete! Report saved to: {output_file}")

# This part tells Python to run the function when we start the script
if __name__ == "__main__":
    run_audit("data/test_data.csv")