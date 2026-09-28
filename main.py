import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == "" or api_key == None:
    raise RuntimeError("API key not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

if response.usage == None:
    raise RuntimeError("Failed to request API")

if args.verbose == True:
    print("User prompt: " + args.user_prompt)
    print("Prompt tokens: " + str(response.usage.prompt_tokens))
    print("Response tokens: " + str(response.usage.completion_tokens))

print(response.choices[0].message.content)
