import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from functions.config import MAX_ITERS

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()


# def main():
#     load_dotenv()

#     verbose = "--verbose" in sys.argv
#     args = [ #safer to store args as a list instead of single element access 
#         arg           # ← this is what gets added to the list
#         for arg in sys.argv[1:]  
#         if not arg.startswith("--")
#         ]

#     if not args:
#         print("AI Code Assistant")
#         print('\nUsage: python main.py "your prompt here" [--verbose]')
#         print('Example: python main.py "How do I build a calculator app?"')
#         sys.exit(1)

#     api_key = os.environ.get("GEMINI_API_KEY")
#     client = genai.Client(api_key=api_key)

#     user_prompt = " ".join(args)

#     if verbose:
#         print(f"User prompt: {user_prompt}\n")

#     messages = [
#         types.Content(role="user", parts=[types.Part(text=user_prompt)]),
#     ]
#     print(f"what is messages type: {type(messages[0])}")

#     for i in range(20):
#         result = generate_content(client, messages, verbose)

#         # Stop if LLM is done reasoning (i.e. gave final response, no function calls)
#         if isinstance(result, str):
#             print("\n Final response:\n")
#             print(result)
#             break
    
#     # for i in range(20):
#     #     response = generate_content(client, messages, verbose)
        
           
#     #     # print(f"response type: {type(response)}")
#     #     # print(f"candidate type: {type(response.candidates)}")
#     #     for candidate in response.candidates:
#     #         # print(f'here: {type(candidate.content)}')
#     #         # print(f'here 2: {candidate.content}')
#     #         print('content: ',candidate.content)
#     #         messages.append(candidate.content)

# def generate_content(client, messages, verbose):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-001",
#         contents=messages,
#         config=types.GenerateContentConfig(
#             tools=[available_functions], 
#             system_instruction=system_prompt
#         ),
#     )

#     if verbose:
#         print("Prompt tokens:", response.usage_metadata.prompt_token_count)
#         print("Response tokens:", response.usage_metadata.candidates_token_count)

#     # ✅ Append LLM response candidates to messages
#     for candidate in response.candidates:
#         messages.append(candidate.content)

#     if not response.function_calls:
#         return False  # No function called — we're done

#     # ✅ Handle function calls and add responses
#     for function_call_part in response.function_calls:
#         function_call_result = call_function(function_call_part, verbose)

#         if (
#             not function_call_result.parts
#             or not function_call_result.parts[0].function_response
#         ):
#             raise Exception("empty function call result")

#         if verbose:
#             print(f"-> {function_call_result.parts[0].function_response.response}")

#         # ✅ Add the function result to the conversation
#         messages.append(
#             types.Content(
#                 role="function",
#                 parts=[function_call_result.parts[0]]
#             )
#         )

#     return True  # Function was called → continue loop


# def generate_content(client, messages, verbose):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-001",
#         contents=messages,
#         config=types.GenerateContentConfig(
#             tools=[available_functions], system_instruction=system_prompt
#         ),
#     )
#     if verbose:
#         print("Prompt tokens:", response.usage_metadata.prompt_token_count)
#         print("Response tokens:", response.usage_metadata.candidates_token_count)

#     if not response.function_calls:
#         return response.text

#     function_responses = []
#     for function_call_part in response.function_calls:
#         function_call_result = call_function(function_call_part, verbose)
#         if (
#             not function_call_result.parts
#             or not function_call_result.parts[0].function_response
#         ):
#             raise Exception("empty function call result")
#         if verbose:
#             print(f"-> {function_call_result.parts[0].function_response.response}")
#         function_responses.append(function_call_result.parts[0])

#     if not function_responses:
#         raise Exception("no function responses generated, exiting.")


# if __name__ == "__main__":
#     main()


    

# def generate_content(client, messages, verbose):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-001",
#         contents=messages,
#         config=types.GenerateContentConfig(
#             tools=[available_functions], 
#             system_instruction=system_prompt #gives the chat a role eg. You are a math professor
#         ), 
#     )
#     #print('response candidate:')
#     #candidate are possible reponses by the llm
#     #print(response.candidates)

#     if verbose:
#         print("Prompt tokens:", response.usage_metadata.prompt_token_count)
#         print("Response tokens:", response.usage_metadata.candidates_token_count)
#     print("Response:")
#     #print(response.text)
#     #print(response.candidates)
#     #response.function_calls returns list of function call objects, 
#     #function_calls[0] is the first function call object. it has property id, args and name
#     if not response.function_calls:
#         return response.text

    
#     for function_call_part in response.function_calls:
#         function_call_result = call_function(function_call_part, verbose)

#         if (
#             not function_call_result.parts
#             or not function_call_result.parts[0].function_response
#         ):
#             raise Exception("empty function call result")

#         result = function_call_result.parts[0].function_response.response

#         if not result:
#              raise Exception("no function responses generated, exiting.")
             
#         if verbose:
#             print(f"-> {result}")
#         else:
#             print(result)
#     #return response



# if __name__ == "__main__":
#     main()