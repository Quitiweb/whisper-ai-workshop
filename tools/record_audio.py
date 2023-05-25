import pyaudio
import wave


def record_audio_to_file(filename):
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    sformat = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 10

    p = pyaudio.PyAudio()
    stream = p.open(format=sformat,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []

    print()
    print("Recording...")
    print()
    print("Seconds left: 10")
    partial_time = 42
    seconds_left = 9

    for i in range(int(sample_rate / chunk * record_seconds)):
        if i > partial_time:
            print(f"Seconds left: {seconds_left}")
            partial_time += 42
            seconds_left -= 1
        data = stream.read(chunk)

        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)

    print()
    print("Finished recording.")
    print()

    stream.stop_stream()
    stream.close()
    p.terminate()

    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sformat))  # set the sample format
    wf.setframerate(sample_rate)  # set the sample rate
    wf.writeframes(b"".join(frames))  # write the frames as bytes

    wf.close()
