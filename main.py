import os,sys
from dotenv import load_dotenv

load_dotenv("gemini-api.env")
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

if (len(sys.argv)==1):
    print("Error: no prompt provided.")
    exit(1)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(model="gemini-2.0-flash-001",
                            contents=messages)

print(response.text)
data = response.usage_metadata
print(f"Prompt tokens: {data.prompt_token_count}\nResponse tokens: {data.candidates_token_count}")