import os
from elevenlabs import set_api_key, voices
from dotenv import load_dotenv
load_dotenv()


set_api_key(os.getenv("ELEVEN_API_KEY"))

voice_list = voices()

for v in voice_list:
    print()
    print(v.voice_id)
    print(v.name)
    print(v.category)

# voice_id = "eVJv3Q6mPjY246dFTov0"
# voice_category = "cloned"
