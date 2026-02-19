import cv2
import time
import json
from ultralytics import YOLO

model = YOLO("yolov8n.pt") #loading the detection model
cap = cv2.VideoCapture(0) #opens webcam (0 -> default camera)

start_time = time.time() #record when the camera started
person_detected = False #final result to save

while True: #run it forever until the user presses Q
    ret, frame = cap.read() #gets an image from the webcam (ret -> did camera work, fram -> actual image)
    if not ret: #if camera fails stop program
        break

    results = model(frame) #send the image to YOLO AI model and the AI returns the detected objects

    
    classes = results[0].boxes.cls.tolist() if results[0].boxes else [] #extract detected classes 

    #check if human exists (YOLO class 0 = person)
    if 0 in classes: 
        person_detected = True

    if person_detected: #specify text depending on if a person is detected
        text = "Human Detected"
    else:
        text = "No Human"

    #show text if humn is detected
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Detection", frame) 

    if time.time() - start_time >= 10: #Stop after 10 seconds
        break

    if cv2.waitKey(1) & 0xFF == ord("q"): #Allow manual quit with Q
        break
        
    data = {"person_detected": person_detected} #store results

    with open("result.txt", "w") as f:
        json.dump(data, f, indent=4)



cap.release() #turns off webcam properly
cv2.destroyAllWindows() #closes the video window
