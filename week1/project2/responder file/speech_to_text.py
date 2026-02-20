import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    
    # --- ADD THIS LINE ---
    # This tells the script: "Don't stop recording until I've been silent for 3 full seconds"
    recognizer.pause_threshold = 3.0 

    try:
        with sr.Microphone() as source:
            print("Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)

            print("Speak now (I will wait 3 seconds after you finish before stopping)...")
            # timeout=None means it waits forever for you to start
            # phrase_time_limit=60 means it captures up to 60 seconds of audio
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=10)

        print("Recognizing...")
        text = recognizer.recognize_google(audio)

        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")
       

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    speech_to_text()
