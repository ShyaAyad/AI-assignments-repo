# pip install numpy opencv-python

import json
import numpy as np
import time
import cv2

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


# ---------- Open Camera ----------
cap = cv2.VideoCapture(0)

print("Press Q to quit")

while True:

    # Read camera frame
    ret, frame = cap.read()
    if not ret:
        break

    # ---------- Read hand_data.txt ----------
    try:
        with open(INPUT_FILE, "r") as f:
            hand_data = json.load(f)
    except:
        hand_data = {"hand_detected": False}

    hand_detected = hand_data.get("hand_detected", False)
    gesture = "None"

    if hand_detected and "landmarks" in hand_data:
        landmarks = hand_data["landmarks"]
        gesture = detect_gesture(landmarks)

    # ---------- Save result ----------
    output_data = {
        "hand_detected": hand_detected,
        "gesture": gesture,
        "timestamp": time.time()
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output_data, f, indent=4)

    # ---------- DISPLAY TEXT ON SCREEN ----------
    cv2.putText(
        frame,
        "Gesture: " + gesture,
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show window
    cv2.imshow("Gesture Detection", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



