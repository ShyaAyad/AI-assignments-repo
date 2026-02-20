import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Adjusting for background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)

            print("Speak now...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

        print("Recognizing...")
        text = recognizer.recognize_google(audio)

        print("You said:", text)

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")

    except sr.RequestError:
        print("Could not request results. Check your internet connection.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    speech_to_text()

    #hi
