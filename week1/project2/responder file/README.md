# Voice AI Assistant Agent 

A multi-agent system that allows you to talk to your laptop. It captures your voice, uses Google’s Gemini AI to generate an intelligent answer, and speaks the response back to you.

## How It Works
The system runs a pipeline of agents in sequence:

1. **Speech to Text** – captures your voice via the microphone and converts it into text (SpeechRecognition)
2. **Brain Agent** – sends the text to Google Gemini AI to generate a smart response
3. **Response Handler** – processes the AI's output and saves the conversation to a file
4. **Text to Speech** – reads the AI’s generated answer aloud so you can hear it

## Prerequisites
- Python 3.12
- pip
- Google Gemini API Key

## Installation

1. Clone the repository
```bash
   git clone <your repo link>
   cd AI-assignments-repo/week1/project2/"responder file"
```

2. Install the required libraries
```bash
   py -3.12 -m pip install SpeechRecognition pyttsx3 pyaudio google-generativeai
```

## Usage
Run the main agent:
```bash
python main.py
```
## Project Structure
```
project2/responder file/
   main.py              Main agent — runs the full voice pipeline
   speech_to_text.py    Listens to your voice via microphone
   response.py          Connects to Gemini AI to get answers
   text_to_speech.py    Reads the AI's answer aloud
   agent.txt            Input: Instructions for the AI's personality
   output.txt           Output: Logs the full AI response
```
