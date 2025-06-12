import os
import sys
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

def load_api_client() -> genai.Client:
	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")
	if not api_key:
		print("Error: GEMINI_API_KEY is not set in .env")
		sys.exit(1)
	return genai.Client(api_key=api_key)

def parse_arguments() -> tuple[str, bool]:
	if len(sys.argv) < 2:
		print("Usage: python main.py <prompt> [--verbose]")
		sys.exit(1)

	verbose = "--verbose" in sys.argv
	prompt_args = [arg for arg in sys.argv[1:] if arg != "--verbose"]
	user_prompt = " ".join(prompt_args)
	return user_prompt, verbose

def build_messages(prompt: str) -> list:
	return [types.Content(role="user", parts=[types.Part(text=prompt)])]

def get_response_with_retries(client, messages, model: str, retries: int = 3, delay: int = 2):
	for attempt in range(1, retries + 1):
		try:
			return client.models.generate_content(model=model, contents=messages)
		except ServerError as e:
			print(f"[Attempt {attempt}] ServerError: {e}")
			if attempt < retries:
				time.sleep(delay)
			else:
				print("All retry attempts failed. Exiting.")
				sys.exit(1)

def display_response(content_response, user_prompt: str, verbose: bool):
	if verbose:
		print(f"User prompt: {user_prompt}")
		print("-" * 40)
		print(content_response.text)
		print("-" * 40)
		print(f"Prompt tokens: {content_response.usage_metadata.prompt_token_count}")
		print(f"Response tokens: {content_response.usage_metadata.candidates_token_count}")
	else:
		print(content_response.text)


def main():
	user_prompt, verbose = parse_arguments()
	client = load_api_client()
	messages = build_messages(user_prompt)
	response = get_response_with_retries(client, messages, model="gemini-2.0-flash-001")
	display_response(response, user_prompt, verbose)


if __name__ == "__main__":
    main()