import openai

openai.api_key = 'your-openai-api-key'

def process_nlp_query(query, df):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Given the dataset: {df.head().to_string()}\nAnswer the following query: {query}",
      max_tokens=150
    )
    return response.choices[0].text.strip()

def handle_query(query, file_path):
    df = pd.read_csv(file_path)
    answer = process_nlp_query(query, df)
    return answer
