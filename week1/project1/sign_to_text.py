
# pip install numpy

import json
import numpy as np
import time

# ---------- Input/Output files ----------
INPUT_FILE = "hand_data.txt"
OUTPUT_FILE = "detected_sign.txt"


# ---------- Finger State Function ----------
def get_finger_state(landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if landmarks[4]['x'] < landmarks[3]['x']:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in tips[1:]:
        if landmarks[tip]['y'] < landmarks[tip - 2]['y']:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


# ---------- Gesture Detection ----------
def detect_gesture(landmarks):
    fingers = get_finger_state(landmarks)

    if fingers == [1,1,1,1,1]:
        return "Open Palm"
    if fingers == [0,0,0,0,0]:
        return "Fist"
    if fingers == [0,1,0,0,0]:
        return "One"
    if fingers == [0,1,1,0,0]:
        return "Two"
    if fingers == [0,1,1,1,0]:
        return "Three"
    if fingers == [1,0,0,0,0]:
        if landmarks[4]['y'] < landmarks[3]['y']:
            return "Thumbs Up"
        else:
            return "Thumbs Down"

    # OK sign
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]

    distance = np.sqrt(
        (thumb_tip['x'] - index_tip['x'])**2 +
        (thumb_tip['y'] - index_tip['y'])**2
    )

    if distance < 0.05:
        return "OK"

    return "Unknown"


# ---------- MAIN LOOP ----------
while True:
    # Read hand_data.txt
    try:
        with open(INPUT_FILE, "r") as f:
            # Check if file is empty before loading
            content = f.read()
            if not content:
                hand_data = {"hand_detected": False}
            else:
                hand_data = json.loads(content)
    except Exception:
        hand_data = {"hand_detected": False}

    hand_detected = hand_data.get("hand_detected", False)
    gesture = "None"

    if hand_detected and "landmarks" in hand_data:
        landmarks = hand_data["landmarks"]
        gesture = detect_gesture(landmarks)

    # Save result to detected_sign.txt
    output_data = {
        "hand_detected": hand_detected,
        "gesture": gesture,
        "timestamp": time.time()
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output_data, f, indent=4)

    # --- THE STOP CONDITION ---
    # We stop the script if a real gesture was found and saved
    if gesture != "None" or hand_detected == False:
        break 

    

    # Small delay
    time.sleep(0.1)





