import tkinter as tk
import winsound
import threading
import time

def play_alarm():
    # Rapid fire beeps
    for _ in range(8):
        winsound.Beep(2500, 150) # Shorter, faster beeps
        time.sleep(0.05)

def trigger_visual_alert():
    root = tk.Tk()
    root.title("Security Alert")
    
    # 1. Full Screen Mode
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg='black')
    
    # 2. Big Red Text
    label = tk.Label(
        root, 
        text="ERROR:\nWRONG MOVEMENT", 
        fg="red", 
        bg="black", 
        font=("Arial", 70, "bold") # Even bigger for full screen
    )
    label.pack(expand=True)

    # 3. Start Sound
    sound_thread = threading.Thread(target=play_alarm)
    sound_thread.daemon = True
    sound_thread.start()

    # 4. Auto-Close Timer (3000 milliseconds = 3 seconds)
    # This makes it "faster" by closing itself automatically
    root.after(3000, root.destroy)

    root.mainloop()

if __name__ == "__main__":
    trigger_visual_alert()