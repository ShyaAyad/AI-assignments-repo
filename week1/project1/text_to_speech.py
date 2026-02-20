# Requirements:
# pip install pyttsx3

import pyttsx3
import os
import json
import sys


INPUT_FILE = "detected_sign.txt"# --- STEP 1: PRE-RUN CHECK (The very beginning) ---


def check_if_should_run():
    if not os.path.exists(INPUT_FILE) or os.path.getsize(INPUT_FILE) == 0:
        sys.exit(0) # Exit if no file or empty

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            gesture = data.get("gesture", "")
            
            if gesture == "Unknown" or gesture == "None":
                # print("Gesture is Unknown. Stopping Agent 6 immediately.")
                sys.exit(0)
    except:
        sys.exit(0) # Exit on any read error to be safe

# Execute the check immediately
check_if_should_run()


class Agent6_TextToVoice:
    def __init__(self,
                 input_file="detected_sign.txt",
                 output_audio="response_audio.wav"):

        self.input_file = input_file
        self.output_audio = output_audio

        # Initialize TTS engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)

        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)

    def clear_files(self):
        """Clear the content of relevant files without deleting them"""
        files_to_clear = [
            "detected_sign.txt",
            "hand_data.txt",
            "result.txt"
        ]

        for file_path in files_to_clear:
            try:
                if os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.truncate(0)
            except:
                pass

    def convert_once_and_exit(self):

        # --- Check if input file exists and is not empty ---
        if not os.path.exists(self.input_file) or os.path.getsize(self.input_file) == 0:
            sys.exit(1)  # Exit with failure code if no data

        try:
            with open(self.input_file, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    sys.exit(1)  # Exit if JSON is invalid

                gesture_text = data.get("gesture", "").strip()

            if not gesture_text:
                sys.exit(1)  # Exit if gesture is empty

            # --- Convert gesture to speech ---
            self.engine.say(gesture_text)
            self.engine.save_to_file(gesture_text, self.output_audio)
            self.engine.runAndWait()

        except Exception:
            sys.exit(1)  # Exit with failure if anything goes wrong

        finally:
            # --- Clear files after TTS ---
            self.clear_files()
            try:
                self.engine.stop()
            except:
                pass

            # Exit code 0 = success
            sys.exit(0)


if __name__ == "__main__":
    agent6 = Agent6_TextToVoice()
    agent6.convert_once_and_exit()
