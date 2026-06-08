import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visuals(file_path):
    print(f"📊 Generating Visual Report for: {file_path}")
    
    # 1. Load data
    df = pd.read_csv(file_path)
    
    # 2. Create a folder for plots if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')
        
    # 3. Create a simple Bar Chart of Categories (or in this case, ages)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='name', y='age', data=df)
    plt.title('Age Distribution of Users')
    
    # 4. Save the plot as a professional image
    plt.savefig('plots/age_distribution.png')
    print("✅ Success! Chart saved in /plots/age_distribution.png")

if __name__ == "__main__":
    create_visuals("data/test_data.csv")