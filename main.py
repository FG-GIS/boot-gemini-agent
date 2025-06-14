import os,sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions,call_function
from config import MAX_ITERS

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
    try:
        generate_content(client,messages, verbose)
    except Exception as e:
        print(f"Error while generating content: {e}")



def generate_content(client, messages, verbose):
    for i in range(MAX_ITERS):
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
            )
        
        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")


        if not response.function_calls:
            print(f"Final response:\n{response.text}")
            return
        
        for cand in response.candidates:
            messages.append(cand.content)

        function_responses = []
        for call in response.function_calls:
                # print(f"Calling function: {call.name}({call.args})")
                function_call_result = call_function(call,verbose)
                if (not function_call_result.parts or not function_call_result.parts[0].function_response.response):
                    raise Exception("Function call error, response empty.")
                messages.append(function_call_result)
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])
        
        if not function_responses:
            raise Exception("No function responses generated, exiting.")
    
    print(f"Max iterations ({MAX_ITERS}) reached.")
    sys.exit(1)



if __name__ == "__main__":
    main()