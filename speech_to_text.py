import speech_recognition as sr
import os

def convert_audio_to_text(filename, output_file="text_from_speech_.txt"):
    recognizer = sr.Recognizer()
    
    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        return

    try:
        with sr.AudioFile(filename) as audio_source:
            recognizer.adjust_for_ambient_noise(audio_source)
            audio_data = recognizer.listen(audio_source)
        
        text = recognizer.recognize_google(audio_data)
        os.remove(filename)  # Remove the audio file after processing
        
        with open(output_file, "a") as file:
            file.write(text + " ")

    except sr.UnknownValueError:
        print(f"Could not understand audio in {filename}.")
    except sr.RequestError as e:
        print(f"Error with Google Speech Recognition service: {e}")
