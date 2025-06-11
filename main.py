import os,sys
from dotenv import load_dotenv

from google import genai
from google.genai import types


def main():
    load_dotenv("gemini-api.env")

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant model -> gemini-2.0-flash-001")
        print('\nUsage: python3 main.py "your prompt here"')
        sys.exit(1)
    user_prompt = " ".join(args)

    # instancing client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client,messages)



def generate_content(client, messages):

    response = client.models.generate_content(model="gemini-2.0-flash-001",
                                contents=messages)
    print(f"Response:\n{response.text}\n")
    data = response.usage_metadata
    print(f"Prompt tokens: {data.prompt_token_count}\nResponse tokens: {data.candidates_token_count}")