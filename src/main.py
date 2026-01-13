from gemini_client import GeminiClient
from prompt_engine import PromptEngine
from response_parser import ResponseParser

def main():
    user_input = input("Enter your prompt: ")

    prompt_engine = PromptEngine()
    final_prompt = prompt_engine.build(user_input)

    client = GeminiClient()
    response = client.send_prompt(final_prompt)

    parser = ResponseParser()
    parsed = parser.parse(response)

    print("\n--- Gemini Response ---")
    print(parsed["raw_output"])

    print("\n--- Metadata ---")
    print(parsed)

if __name__ == "__main__":
    main()