import os
import time
import threading

from record_audio import record_audio
from speech_to_text import convert_audio_to_text
from text_processing import process_text


def main():
    audio_segments=3  # Number of audio segments to record
    record_duration=10  # Duration for each recording in seconds

    for i in range(audio_segments):
        filename=f"record{i}.wav"

        # Record audio in a separate thread
        record_thread=threading.Thread(target=record_audio, args=(filename, record_duration))
        record_thread.start()
        record_thread.join()  # Ensure recording completes before starting conversion

        # Give a slight delay to ensure file I/O completes
        time.sleep(0.1)

        # Convert audio to text after recording
        convert_audio_to_text(filename)

    # Ensure that 'test.txt' and 'text_from_speech_.txt' files exist before processing
    if not os.path.exists("test.txt") or not os.path.exists("text_from_speech_.txt"):
        print("Error: Either 'test.txt' or 'text_from_speech_.txt' is missing. Please ensure both files exist.")
        return

    # Process the resulting text and compare with the questions
    recorded_words=process_text("text_from_speech_.txt")
    question_words=process_text("test.txt")

    common_words=set(recorded_words).intersection(set(question_words))

    print(f"Number of common words: {len(common_words)}")
    print(f"Common words: {common_words}")


if __name__ == "__main__":
    main()
