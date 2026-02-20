import subprocess
import os

base = os.path.dirname(os.path.abspath(__file__))

# # 1
try:
    subprocess.run(["python",  os.path.join(base, "human_detector_agent.py")], timeout=15)
except subprocess.TimeoutExpired:
    pass

# # 3
try:
    subprocess.run(["python",  os.path.join(base, "hands_detector.py")], timeout=20)
except subprocess.TimeoutExpired:
    pass

# # 5

try:
    subprocess.run(["python", os.path.join(base, "sign_to_text.py")])
except subprocess.TimeoutExpired:
    pass


# # 4

try:
    result = subprocess.run(
        ["python", os.path.join(base, "alert_agnet.py")]
    )
except:
    pass


# 6 
try:
 subprocess.run(["python", os.path.join(base, "text_to_speech.py")])      
except subprocess.TimeoutExpired:
        pass

# 7
try:
    subprocess.run(["python", os.path.join(base, "cleaner.py")])
except subprocess.TimeoutExpired:
    pass
