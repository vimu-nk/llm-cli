import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def ask_question(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    print("🔍 Ask your question (Ctrl+C to exit):")
    while True:
        try:
            question = input("\n> ")
            answer = ask_question(question)
            print(f"\n🧠 Answer:\n{answer}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
