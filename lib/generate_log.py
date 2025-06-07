# lib/generate_log.py

from datetime import datetime

def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    # STEP 2: Create filename based on date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write data to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Return the filename
    return filename


if __name__ == "__main__":
    sample_log = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_log)
