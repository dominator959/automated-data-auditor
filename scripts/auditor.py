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
    
    # 4. Check for duplicates safely
    if 'name' in df.columns:
        duplicate_count = df.duplicated(subset=['name']).sum()
    elif 'item' in df.columns:
        duplicate_count = df.duplicated(subset=['item']).sum()
    else:
        duplicate_count = df.duplicated().sum()
    
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
    # 1. List files available in the data folder
    print("Files available in /data folder:")
    files = os.listdir("data")
    for f in files:
        if f.endswith(".csv"):
            print(f"- {f}")
            
    # 2. Ask user for input
    user_file = input("\nEnter the name of the file you want to audit (e.g., test_data.csv): ")
    
    # 3. Build the full path
    full_path = os.path.join("data", user_file)
    
    # 4. Check if file exists before running
    if os.path.exists(full_path):
        run_audit(full_path)
    else:
        print(f"❌ Error: The file '{user_file}' was not found in the /data folder.")