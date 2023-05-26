import os
import openai
import tempfile
from dotenv import load_dotenv
from elevenlabs import play


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
eleven_api_key = os.getenv("ELEVEN_API_KEY")


chatgpt_model = "gpt-3.5-turbo"
chatgpt_system = "You are a helpful assistant on a conversation. Answer should be not too long. Be ironic and acid"

selected_voice_id = "eVJv3Q6mPjY246dFTov0"


# Function to get GPT-4 response
def get_gpt4_response(prompt):
    response = openai.ChatCompletion.create(
        model=chatgpt_model,
        messages=[
            {"role": "system", "content": chatgpt_system},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# Main function to interact with GPT-4
def interact_with_gpt4(prompt):
    response_text = get_gpt4_response(prompt)

    import requests

    chunk_size = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + selected_voice_id

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": eleven_api_key
    }

    data = {
        "text": response_text,
        "model_id": "eleven_multilingual_v1",
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 1.0
        }
    }

    response = requests.post(url, json=data, headers=headers)

    # Save audio data to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
        f.flush()
        temp_filename = f.name

    return temp_filename


# Function to continuously interact with GPT-4
def continuous_interaction():
    while True:
        # clear_output(wait=True)
        prompt = input("Enter your prompt (or type 'exit' to stop): ")
        if prompt.lower() == 'exit':
            break
        audio_file = interact_with_gpt4(prompt)
        play(audio_file, notebook=True)


# Example usage
continuous_interaction()
