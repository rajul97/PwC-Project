import openai

openai.api_key = "your_openai_api_key"

def ask_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(ask_ai("What is AI?"))
