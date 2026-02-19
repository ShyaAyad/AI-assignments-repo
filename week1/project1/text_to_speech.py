import pyttsx3
import os
import time

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
        self.engine.setProperty('voice', voices[0].id)  # 0=male, 1=female

        # Track last processed text
        self.last_text = ""

    def wait_and_convert(self):
        print("Agent 6 Running...")
        print("Monitoring file:", os.path.abspath(self.input_file))
        print("--------------------------------\n")

        while True:
            try:
                # Wait until the file exists
                if not os.path.exists(self.input_file):
                    print(f"Waiting for Agent 5 output: '{self.input_file}' not found yet...")
                    time.sleep(2)
                    continue

                # Wait until the file has content
                if os.path.getsize(self.input_file) == 0:
                    print("Waiting for Agent 5 output...")
                    time.sleep(1)
                    continue

                # Read text from Agent 5
                with open(self.input_file, "r", encoding="utf-8") as file:
                    text = file.read().strip()

                # Only process new text
                if text and text != self.last_text:
                    print("Detected new text from Agent 5:", text)

                    # Speak the text
                    self.engine.say(text)
                    self.engine.runAndWait()

                    # Save audio
                    self.engine.save_to_file(text, self.output_audio)
                    self.engine.runAndWait()
                    print("Audio saved as:", self.output_audio)

                    # Clear the file
                    with open(self.input_file, "w", encoding="utf-8") as file:
                        file.write("")
                        file.flush()

                    print(f"'{self.input_file}' cleared successfully.\nWaiting for new input...\n")

                    # Remember last processed text
                    self.last_text = text

                time.sleep(0.5)

            except Exception as e:
                print("Error occurred:", e)
                time.sleep(2)


if __name__ == "__main__":
    agent6 = Agent6_TextToVoice()
    agent6.wait_and_convert()
