import pyaudio
import wave

def record_audio(filename, duration=10, sample_rate=44100, channels=1):
    frame_size = 1024  # determines no. of samples per frame
    sample_format = pyaudio.paInt16  # Audio format
    audio_interface = pyaudio.PyAudio()
    
    # Open a stream for recording
    stream = audio_interface.open(format=sample_format, channels=channels, rate=sample_rate, 
                                  frames_per_buffer=frame_size, input=True)
    frames = []

    for _ in range(0, int(sample_rate / frame_size * duration)):
        data = stream.read(frame_size)
        frames.append(data)

    # Save the recorded frames to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio_interface.get_sample_size(sample_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    stream.stop_stream()
    stream.close()
    audio_interface.terminate()
