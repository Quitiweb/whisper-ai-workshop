import os
import time
from urllib.error import HTTPError

import openai
from dotenv import load_dotenv
from openai._exceptions import RateLimitError

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# GPT_MODEL = "gpt-4"
# GPT_MODEL = "gpt-4-32k"
GPT_MODEL = "gpt-4-1106-preview"

client = openai.OpenAI()


def get_openai_models():
    res = openai.Model.list()
    for r in res.data:
        print(r.id)


def chat_con_gpt(mensaje, conversation, description, tokens):
    retries = 5
    print()
    print("Longitud actual: ", tokens)
    print()
    conversation += mensaje + "\nPersona: "

    ntries = 0
    error = True
    while (ntries < retries) and error:
        try:
            response = client.chat.completions.create(
                model=GPT_MODEL,
                messages=[
                    {"role": "system", "content": description},
                    {"role": "user", "content": conversation},
                ]
            )
            error = False
        except (HTTPError, RateLimitError) as e:
            error = True
            ntries += 1
            print("Error de openai: {}".format(e))
            print()
            for i in range(5, -1, -1):
                print("Reintentando en: {}".format(i))
                time.sleep(1)

    result = ""
    for option in response.choices:
        result += option.message.content

    conversation += result + "\nPersona: "

    tokens = response.usage.total_tokens

    return result, conversation, tokens
