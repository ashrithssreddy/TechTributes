import openai
import yaml

# Load credentials from config.yaml
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# OpenAI API Key
openai.api_key = config['openai']['api_key']

def generate_poem(prompt, model="gpt-3.5-turbo", max_tokens=300):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()
