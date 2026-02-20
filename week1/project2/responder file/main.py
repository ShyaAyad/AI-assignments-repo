import subprocess
import os

# Get the absolute path to the directory where this script is located
base = os.path.dirname(os.path.abspath(__file__))

# 1. Speech to Text
try:
    subprocess.run(["python", os.path.join(base, "speech_to_text.py")])
except subprocess.TimeoutExpired:
    pass

# 2. Response (Gemini Agent)
try:
    subprocess.run(["python", os.path.join(base, "response.py")])
except subprocess.TimeoutExpired:
    pass

# 3. Text to Speech
try:
    subprocess.run(["python", os.path.join(base, "text_to_speech.py")])
except subprocess.TimeoutExpired:
    pass
