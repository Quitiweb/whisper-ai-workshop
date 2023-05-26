import os

import requests
from dotenv import load_dotenv
from elevenlabs import set_api_key, voices

load_dotenv()
selected_voice_id = "eVJv3Q6mPjY246dFTov0"
eleven_api_key = os.getenv("ELEVEN_API_KEY")


def text_to_vclone(text_in, audio_path):
    chunk_size = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + selected_voice_id

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": eleven_api_key
    }
    data = {
        "text": text_in,
        "model_id": "eleven_multilingual_v1",
        "voice_settings": {
            "stability": 0.8,
            "similarity_boost": 0.8
        }
    }
    response = requests.post(url, json=data, headers=headers)

    with open(audio_path, "wb") as output:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                output.write(chunk)


def print_my_voices():
    set_api_key(eleven_api_key)
    voice_list = voices()
    for v in voice_list:
        print()
        print(v.voice_id)
        print(v.name)
        print(v.category)

# voice_id = "eVJv3Q6mPjY246dFTov0"
# voice_category = "cloned"
