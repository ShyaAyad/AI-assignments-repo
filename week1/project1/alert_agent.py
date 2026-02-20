import tkinter as tk
import winsound
import threading
import time
import json
import os
import sys

# ---------- 1. PRE-RUN CHECK ----------
OUTPUT_FILE = "detected_sign.txt"

if os.path.exists(OUTPUT_FILE):
    try:
        with open(OUTPUT_FILE, "r") as f:
            data = json.load(f)

            if data.get("gesture") != "Unknown" or data.get("gesture") == "None":
                sys.exit()
    except:
        sys.exit()
else:
    sys.exit()

# ---------- 2. ALERT LOGIC ----------

def play_alarm():
    for _ in range(4):
        winsound.Beep(2000, 50)
        time.sleep(0.05)

def clear_files():
    files_to_clear = [
        "result.txt",
        "hand_data.txt",
        "detected_sign.txt"
    ]

    for file in files_to_clear:
        try:
            if os.path.exists(file):
                open(file, "w").close()   # Clears file content
        except:
            pass

def trigger_visual_alert():
    root = tk.Tk()
    root.title("Security Alert")

    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg='black')

    label = tk.Label(
        root,
        text="ERROR:\nWRONG MOVEMENT",
        fg="red",
        bg="black",
        font=("Arial", 70, "bold")
    )
    label.pack(expand=True)

    sound_thread = threading.Thread(target=play_alarm)
    sound_thread.daemon = True
    sound_thread.start()

    # After 3 seconds:
    root.after(3000, lambda: [clear_files(), root.destroy()])

    root.mainloop()

if __name__ == "__main__":
    trigger_visual_alert()
