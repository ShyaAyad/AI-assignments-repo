import google.generativeai as genai
import os
import sys

# 1. Setup API
genai.configure(api_key="AIzaSyCrGZwRvAOJCIecV86utZWbm783D4fPBmo") # Keep your key safe!
model = genai.GenerativeModel('gemini-2.5-flash') 

USER_FILE = "output.txt"
AGENT_FILE = "agent.txt"

def run_agent():
    try:
        # Check if file exists and has content
        if not os.path.exists(USER_FILE):
            return

        with open(USER_FILE, 'r') as f:
            content = f.read().strip()

        if content:
            # Check if the user wants to STOP
            if content.lower() in ['exit', 'stop', 'quit']:
                with open(USER_FILE, 'w') as f: f.write("") 
                sys.exit() 

            # Request answer
            prompt = f"{content} (Answer in exactly 10 to 15 words.)"
            response = model.generate_content(prompt)
            
            # Clear user file first
            with open(USER_FILE, 'w') as f:
                f.write("")

            # Write answer to output.txt
            with open(AGENT_FILE, 'w') as f:
                f.write(response.text.strip())
            

    except Exception as e:
        print(f"Error: {e}")
        with open(USER_FILE, 'w') as f: f.write("")

if __name__ == "__main__":
    run_agent()
    # The script ends here automatically
