# PROGRAM 2: THE READER

try:
    # HOW: We open the exact same file, but this time with 'r' for Read mode.
    # WHY: Read mode prevents us from accidentally deleting or overwriting the data.
    # REAL-LIFE USAGE: Opening a user's local configuration file to see what theme (dark/light) they prefer.
    with open("my_notes.txt", "r") as file:
        
        # HOW: We suck all the text out of the file and lock it into a variable.
        saved_text = file.read()
        
        print("--- FILE CONTENTS ---")
        print(saved_text)
        
# HOW: We intercept the crash that happens if you try to read a file that doesn't exist yet.
except FileNotFoundError:
    print("[ERROR] The file does not exist yet. Run Program 1 first!")