import subprocess

# # 1
try:
    subprocess.run(["python", "human_detector_agent.py"], timeout=15)
except subprocess.TimeoutExpired:
    pass

# # 3
try:
    subprocess.run(["python", "hands_detector.py"], timeout=20)
except subprocess.TimeoutExpired:
    pass

# # 5

try:
    subprocess.run(["python", "sign_to_text.py"])
except subprocess.TimeoutExpired:
    pass


# # 4

try:
    result = subprocess.run(
        ["python", "alert_agnet.py"]
    )
except:
    pass


# 6 
try:
 subprocess.run(["python", "text_to_speech.py"])      
except subprocess.TimeoutExpired:
        pass

# 7
try:
    subprocess.run(["python", "cleaner.py"])
except subprocess.TimeoutExpired:
    pass
