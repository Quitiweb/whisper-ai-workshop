import whisper


def audio_to_text(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio, fp16=False)
    return result["text"]
