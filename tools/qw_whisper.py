import whisper


def audio_to_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    return result["text"]
