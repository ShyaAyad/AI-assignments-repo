import cv2
import json
from ultralytics import YOLO

model = YOLO("yolov8n.pt") #loading the detection model
cap = cv2.VideoCapture(0) #opens webcam (0 -> default camera)

while True: #run it forever until the user presses Q
    ret, frame = cap.read() #gets an image from the webcam (ret -> did camera work, fram -> actual image)
    if not ret: #if camera fails stop program
        break

    results = model(frame) #send the image to YOLO AI model and the AI returns the detected objects

    
    classes = results[0].boxes.cls.tolist() if results[0].boxes else [] #extract detected classes 

    #check if human exists (YOLO class 0 = person)
    person_detected = 0 in classes

    #prepare JSON data
    data = {"person_detected": person_detected}

    with open("state.json", "w") as f: #opens a file named state.json
        json.dump(data, f) #saves results into the file 

    if person_detected: #specify text depending on if a person is detected
        text = "Human Detected"
    else:
        text = "No Human"

    #show text if humn is detected
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Detection", frame) #draws boxes around detected objects

    if cv2.waitKey(1) & 0xFF == ord("q"): #if user presses Q exit loop
        break

cap.release() #turns off webcam properly
cv2.destroyAllWindows() #closes the video window
