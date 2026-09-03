import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
)

GREEN = "\033[92m"
RESET = "\033[0m"

print("\nEMERIE AI TERMINAL")
print ("Type 'exit' to quit.\n")

while True:
    question = input("You >")

    if question.lower() == "exit":
        break

    
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {"role": "user", "content": question}
    ]

    )

    print ("\nAI >", GREEN + response.choices[0].message.content + RESET)