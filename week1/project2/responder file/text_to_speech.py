import pyttsx3   
import os
import sys # Added for a clean exit

class Agent6_TextToVoice:
    def __init__(self,
                 input_file="agent.txt",
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

    def process_and_exit(self):
        # 1. Check if file exists
        if not os.path.exists(self.input_file):
            return

        # 2. Check if file is empty
        if os.path.getsize(self.input_file) == 0:
            return

        try:
            # 3. Read text
            with open(self.input_file, "r", encoding="utf-8") as file:
                text = file.read().strip()

            if text:
                
                # 4. Speak and Save
                self.engine.say(text)
                self.engine.save_to_file(text, self.output_audio)
                self.engine.runAndWait()

                # 5. Clear the file after reading
                with open(self.input_file, "w", encoding="utf-8") as file:
                    file.write("")
                
            
        except Exception as e:
            pass

if __name__ == "__main__":
    agent6 = Agent6_TextToVoice()
    agent6.process_and_exit() # This runs once and the script ends naturally