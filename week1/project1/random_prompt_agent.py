import time
import random

prompts = [
    "Please move your hand",
    "Wave your hand",
    "Show a thumbs up",
    "Please blink"
]

print("Random Prompt Agent Started...")

last_movement_time = time.time()

while True:
    current_time = time.time()

    # Check if 30 seconds passed
    if current_time - last_movement_time > 30:
        prompt = random.choice(prompts)
        print("\n⚠ No movement detected!")
        print("Random Prompt:", prompt)
        last_movement_time = current_time

    # Small delay so CPU is not overloaded
    time.sleep(1)
