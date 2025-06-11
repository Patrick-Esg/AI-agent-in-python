import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
main = "gemini-2.0-flash-001"
content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(model = main, contents = content)
prompt_token = response.usage_metadata.prompt_token_count
candidate_tokens = response.usage_metadata.candidates_token_count

print(response.text)
print("Prompt tokens:", prompt_token)
print("Response tokens:", candidate_tokens)