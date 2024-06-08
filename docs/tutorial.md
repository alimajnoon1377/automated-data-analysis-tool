# Automated Data Analysis Tool Tutorial

## Introduction

This tutorial guides you through the process of setting up and using the Automated Data Analysis Tool. This tool automatically analyzes datasets and provides comprehensive reports, including visualizations, statistical analyses, and potential insights using natural language processing (NLP).

## Prerequisites

- Python 3.x installed
- `pip` package manager installed

## Setup

1. Clone the repository
    ```bash
    git clone httpsgithub.comyour-usernameautomated-data-analysis-tool.git
    cd automated-data-analysis-tool
    ```

2. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

3. Set up OpenAI API key
    - Obtain an API key from OpenAI.
    - Set the API key in the `srcnlp_processing.py` file
      ```python
      openai.api_key = 'your-openai-api-key'
      ```

## Running the Tool

### Command Line Interface

1. Place your dataset in the `data` directory.
2. Run the main script
    ```bash
    python srcmain.py
    ```

### Web Interface

1. Run the Flask app
    ```bash
    python appapp.py
    ```
2. Open your browser and go to `http127.0.0.15000`.
3. Upload a CSV file and analyze the data.
4. Ask questions about your data in plain English.

## Conclusion

This tutorial covered the basics of setting up and using the Automated Data Analysis Tool. For more detailed usage, refer to the usage guide.
