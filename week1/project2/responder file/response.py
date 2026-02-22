import google.generativeai as genai
import os
import sys

#API key
genai.configure(api_key="AIzaSyCrGZwRvAOJCIecV86utZWbm783D4fPBmo") 
model = genai.GenerativeModel('gemini-2.5-flash') 

USER_FILE = "output.txt"
AGENT_FILE = "agent.txt"

def run_agent():
    try:
        # Checks if file exists and has content
        if not os.path.exists(USER_FILE):
            return

        with open(USER_FILE, 'r') as f:
            content = f.read().strip()

        if content:
            # Checks if the user wants to STOP
            if content.lower() in ['exit', 'stop', 'quit']:
                with open(USER_FILE, 'w') as f: f.write("") 
                sys.exit() 

            # Requests answer
            prompt = f"{content} (Answer in exactly 10 to 15 words.)"
            response = model.generate_content(prompt)
            
            # Clears user file first
            with open(USER_FILE, 'w') as f:
                f.write("")

            # Writes answer to agent.txt
            with open(AGENT_FILE, 'w') as f:
                f.write(response.text.strip())
            

    except Exception as e:
        print(f"Error: {e}")
        with open(USER_FILE, 'w') as f: f.write("")

if __name__ == "__main__":
    run_agent()
