import google.generativeai as genai
import time
import os
import sys

# 1. Setup API
genai.configure(api_key="AIzaSyCIjhOmWRIBUNr7mk-6PP9YSfv7HVFXndw")
model = genai.GenerativeModel('gemini-2.5-flash-lite') # Or 'gemini-1.5-flash'

USER_FILE = "user.txt"
AGENT_FILE = "agent.txt"

def run_agent():
    print("--- Agent is LIVE ---")
    print("Instructions:")
    print("1. Write your question in 'user.txt' and save it.")
    print("2. Type 'exit' in 'user.txt' to stop the program.")
    print("---------------------")

    while True:
        try:
            with open(USER_FILE, 'r') as f:
                content = f.read().strip()

            if content:
                # Check if the user wants to STOP
                if content.lower() in ['exit', 'stop', 'quit']:
                    print("Shutdown command received. Goodbye!")
                    with open(USER_FILE, 'w') as f: f.write("") # Clear file
                    sys.exit() # This closes the program

                print(f"Processing: {content}")
                
                # Request answer
                prompt = f"{content} (Answer in exactly 10 to 15 words.)"
                response = model.generate_content(prompt)
                
                # Clear user.txt first
                with open(USER_FILE, 'w') as f:
                    f.write("")

                # Write answer to agent.txt
                with open(AGENT_FILE, 'w') as f:
                    f.write(response.text.strip())
                
                print(">>> Answer saved to agent.txt!")
                print(">>> Waiting for your next question in user.txt...")

        except Exception as e:
            print(f"Error: {e}")
            with open(USER_FILE, 'w') as f: f.write("")

        time.sleep(2)

if __name__ == "__main__":
    run_agent()