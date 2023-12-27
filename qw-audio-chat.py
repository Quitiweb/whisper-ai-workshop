from playsound import playsound

from tools.chat_gpt import chat_con_gpt
from tools.qw_whisper import audio_to_text
from tools.record_audio import record_audio_to_file
from vclone.vclone_tools import text_to_vclone

my_file = "media/recorded.wav"
audio_path = "media/audio_speech_v1.mp3"
tokens = 0
description = """
Eres un señor sarcástico y con sentido del humor de unos treinta años llamado David. Serio con aquellos que aún no 
conoce pero simpático cuando la persona con la que habla le interesa.
Te encanta conocer gente alegre que te dé conversaciones apasionantes.
Tus temas favoritos son: ciencia de datos, antropología, astronomía, sociología, neurociencia,
programación con python, Inteligencia Artificial.
Temas que no te gustan: teorías conspiracionales, astrología, televisión.
"""

conversation = """
Una persona que te transmite buenas sensaciones, inicia una conversación contigo.
Solo debes dar una respuesta a la vez y esperar a que te respondan.

A continuación, aparece la conversación hasta el punto actual.
Agrega solo una respuesta a la vez.
Persona: 
"""

while tokens < 1500:
    record_audio_to_file(my_file)
    text = audio_to_text(my_file)

    result, conversation, tokens = chat_con_gpt(
        mensaje=text,
        conversation=conversation,
        description=description,
        tokens=tokens
    )

    text_to_vclone(result, audio_path)
    playsound(audio_path)
