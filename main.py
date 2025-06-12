import os,sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

from prompts import system_prompt

def main():
    load_dotenv("gemini-api.env")

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant model -> gemini-2.0-flash-001")
        print('\nUsage: python main.py "your prompt here" [--verbose]\n')
        sys.exit(1)
    user_prompt = " ".join(args)

    # instancing client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client,messages, verbose)



def generate_content(client, messages, verbose):

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=get_available_functions(), system_instruction=system_prompt)
        )
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    foo_calls = response.function_calls
    if foo_calls:
        for call in foo_calls:
            print(f"Calling function: {call.name}({call.args})")
    print(f"Response:\n{response.text}\n")

def get_available_functions():
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
    return [available_functions]

if __name__ == "__main__":
    main()