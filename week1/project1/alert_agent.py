import tkinter as tk  # Imports the toolkit for creating the visual pop-up window
import winsound        # Imports the library to generate system beep sounds on Windows
import threading       # Imports threading to run the alarm sound and UI simultaneously
import time            # Imports time for controlling the duration of the beep pulses
import json            # Imports JSON to parse the gesture data from the previous agent
import os              # Imports the OS module for file existence and size checks
import sys             # Imports sys to handle immediate script termination

# ---------- 1. PRE-RUN CHECK ----------
OUTPUT_FILE = "detected_sign.txt"  # Defines the input file that triggers the alert

if os.path.exists(OUTPUT_FILE):  # Checks if the gesture detection file exists on disk
    try:
        with open(OUTPUT_FILE, "r") as f:  # Opens the file in read mode
            data = json.load(f)  # Parses the JSON string into a Python dictionary

            # If the gesture is valid (not Unknown) or is None, this agent is not needed
            if data.get("gesture") != "Unknown" or data.get("gesture") == "None":
                sys.exit()  # Stops the script immediately
    except:
        sys.exit()  # Exits if there is any error reading or parsing the file
else:
    sys.exit()  # Exits if the file is missing entirely

# ---------- 2. ALERT LOGIC ----------

def play_alarm():  # Function to handle the audible part of the alert
    for _ in range(4):  # Loops four times to create a pulsing alarm effect
        winsound.Beep(2000, 50)  # Plays a 2000Hz tone for 50 milliseconds
        time.sleep(0.05)  # Pauses for 50 milliseconds between beeps

def clear_files():  # Function to reset the system for the next detection cycle
    files_to_clear = [  # List of all communication files to be wiped
        "result.txt",
        "hand_data.txt",
        "detected_sign.txt"
    ]

    for file in files_to_clear:  # Iterates through each file path
        try:
            if os.path.exists(file):  # Checks if the file exists before attempting to clear it
                open(file, "w").close()   # Opens in write mode and closes immediately to empty it
        except:
            pass  # Skips if a file is currently locked or inaccessible

def trigger_visual_alert():  # Function to create and display the full-screen warning
    root = tk.Tk()  # Initializes the main Tkinter window
    root.title("Security Alert")  # Sets the window title

    root.attributes("-fullscreen", True)  # Forces the window to cover the entire screen
    root.attributes("-topmost", True)     # Ensures the window stays on top of all other programs
    root.configure(bg='black')            # Sets the background color to black

    label = tk.Label(  # Creates a text element for the warning
        root,
        text="ERROR:\nWRONG MOVEMENT",  # The specific error message to display
        fg="red",                      # Sets the text color to red
        bg="black",                    # Matches the label background to the window
        font=("Arial", 70, "bold")      # Sets the font type, size, and weight
    )
    label.pack(expand=True)  # Centers the label in the middle of the screen

    sound_thread = threading.Thread(target=play_alarm)  # Prepares the sound function to run in the background
    sound_thread.daemon = True  # Allows the thread to be killed automatically when the window closes
    sound_thread.start()        # Starts the alarm sound immediately

    # After 3 seconds (3000ms):
    # Executes file cleanup and closes the window automatically
    root.after(3000, lambda: [clear_files(), root.destroy()])

    root.mainloop()  # Starts the UI event loop to keep the window visible

if __name__ == "__main__":  # Checks if this script is being run directly
    trigger_visual_alert()  # Calls the main alert function
