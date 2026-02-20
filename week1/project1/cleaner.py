import os

# Define the files used by your agents
FILES_TO_CLEAN = [
    "detected_sign.txt",
    "hand_data.txt",
    "result.txt"
]

def clean_system_files():
    
    for file_path in FILES_TO_CLEAN:
        try:
            if os.path.exists(file_path):
                # Using 'w' mode and truncate(0) ensures the file stays 
                # but all text inside is deleted.
                with open(file_path, "w", encoding="utf-8") as f:
                    f.truncate(0)
            else:
                # If the file doesn't exist, create an empty one
                with open(file_path, "w", encoding="utf-8") as f:
                    pass
                
        except Exception as e:
            pass


if __name__ == "__main__":
    clean_system_files()