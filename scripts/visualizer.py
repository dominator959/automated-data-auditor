import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visuals():
    # 1. Let the user choose the file
    print("Available files in /data:")
    print(os.listdir("data"))
    user_file = input("Which file to visualize? ")
    full_path = os.path.join("data", user_file)

    if not os.path.exists(full_path):
        print("File not found!")
        return

    df = pd.read_csv(full_path)
    
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # 2. Dynamic Plotting Logic
    plt.figure(figsize=(10, 6))
    
    if 'age' in df.columns:
        sns.barplot(x='name', y='age', data=df)
        plt.title(f'Age Analysis: {user_file}')
        save_path = 'plots/age_plot.png'
    elif 'price' in df.columns:
        sns.barplot(x='item', y='price', data=df)
        plt.title(f'Price Analysis: {user_file}')
        save_path = 'plots/price_plot.png'
    else:
        print("No plottable columns (age/price) found!")
        return

    plt.savefig(save_path)
    print(f"✅ Success! Chart saved to {save_path}")

if __name__ == "__main__":
    create_visuals()