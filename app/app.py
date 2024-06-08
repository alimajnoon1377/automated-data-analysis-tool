from flask import Flask, request, render_template, jsonify
from src.main import analyze_data, handle_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    file_path = f"data/{file.filename}"
    file.save(file_path)
    
    summary = analyze_data(file_path, 'reports')
    return render_template('report.html', summary=summary.to_html(), visualizations='reports/pairplot.png')

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    answer = handle_query(query, 'data/sample_data.csv')
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)
