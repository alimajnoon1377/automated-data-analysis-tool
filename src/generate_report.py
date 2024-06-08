from jinja2 import Template

def generate_html_report(summary, visualizations, output_path):
    html_template = """
    <html>
    <head><title>Data Analysis Report</title></head>
    <body>
        <h1>Data Analysis Report</h1>
        <h2>Summary Statistics</h2>
        <pre>{{ summary }}</pre>
        <h2>Visualizations</h2>
        <img src="{{ visualizations }}" alt="Pairplot">
    </body>
    </html>
    """
    template = Template(html_template)
    html_content = template.render(summary=summary.to_string(), visualizations=visualizations)
    
    with open(output_path, 'w') as f:
        f.write(html_content)

def create_report(summary, output_dir):
    generate_html_report(summary, f"{output_dir}/pairplot.png", f"{output_dir}/report.html")
