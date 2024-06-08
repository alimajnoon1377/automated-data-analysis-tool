import os
from data_analysis import analyze_data
from nlp_processing import handle_query
from generate_report import create_report

DATA_PATH = 'data/sample_data.csv'
OUTPUT_DIR = 'reports/'

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Analyze data and generate summary
    summary = analyze_data(DATA_PATH, OUTPUT_DIR)
    
    # Generate HTML report
    create_report(summary, OUTPUT_DIR)
    
    # Handle user query
    user_query = "What is the correlation between variables?"
    answer = handle_query(user_query, DATA_PATH)
    print("NLP Query Answer:", answer)

if __name__ == "__main__":
    main()
