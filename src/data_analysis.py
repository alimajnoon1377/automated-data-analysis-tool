import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def generate_summary_statistics(df):
    return df.describe()

def generate_visualizations(df, output_dir):
    sns.pairplot(df)
    plt.savefig(f"{output_dir}/pairplot.png")

def analyze_data(file_path, output_dir):
    df = load_data(file_path)
    summary = generate_summary_statistics(df)
    generate_visualizations(df, output_dir)
    return summary
