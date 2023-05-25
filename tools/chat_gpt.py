import os
import openai

from dotenv import load_dotenv
load_dotenv()

# openai.organization = "CSW"
openai.api_key = os.getenv("OPENAI_API_KEY")

# print(openai.Model.list())


def chat_con_gpt(mensaje, conversation, description, tokens):
    print()
    print("Longitud actual: ", tokens)
    print()
    conversation += mensaje + "\nPersona: "

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": description},
            {"role": "user", "content": conversation},
        ]
    )
    result = ""
    for option in response.choices:
        result += option.message.content

    conversation += result + "\nPersona: "

    tokens = response["usage"]["total_tokens"]

    return result, conversation, tokens
