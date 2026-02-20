# Sign Detector Agent 

A multi-agent system that detects a person via webcam, recognizes hand signs, 
converts them to text, and reads them aloud using text-to-speech.

## How It Works
The system runs a pipeline of agents in sequence:

1. **Human Detector** – detects if a person is present using the webcam (YOLOv8)
2. **Hand Detector** – captures and tracks hand landmarks using MediaPipe
3. **Sign to Text** – interprets the hand signs and saves them to a file
4. **Alert Agent** – triggers a beep sound and shows an error message if the detected sign is not recognized by the program
5. **Text to Speech** – reads the detected sign aloud

## Prerequisites
- Python 3.12
- pip

## Installation

1. Clone the repository
```bash
   git clone <your repo link>
   cd AI-assignments-repo/week1/project1
```

2. Install the required libraries
```bash
   pip install mediapipe ultralytics numpy pyttsx3
```

## Usage
Run the main agent:
```bash
python main.py
```

## Project Structure
```
project1/
├── main.py                  # Main agent — runs the full pipeline
├── human_detector_agent.py  # Detects human presence via YOLOv8
├── hands_detector.py        # Detects hand landmarks via MediaPipe
├── sign_to_text.py          # Converts signs to text
├── alert_agent.py           # Triggers alerts 
├── text_to_speech.py        # Reads text aloud
├── hand_data.txt            # Output: detected hand data 
├── detected_sign.txt        # Output: detected sign label
├── result.txt               # Output: detected human state (boolean)
└── yolov8n.pt               # YOLOv8 model weights
```