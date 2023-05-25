from playsound import playsound

from tools.qw_whisper import audio_to_text
from tools.record_audio import record_audio_to_file
from tools.text_to_speech import text_to_audio_file

my_file = "media/recorded.wav"
audio_path = "media/audio_speech_v1.mp3"

record_audio_to_file(my_file)

text = audio_to_text(my_file)
text_to_audio_file(text, audio_path)

playsound(audio_path)
