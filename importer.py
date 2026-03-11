# PROGRAM 4: THE JSON IMPORTER

import json

try:
    # HOW: Open the JSON file in Read mode.
    with open("save_game.json", "r") as file:
        
        # HOW: json.load() pulls the text from the file and magically resurrects it back into a live Python Dictionary.
        # WHY: So our code can actually interact with the data (like doing math or lookups) instead of just reading raw text.
        # REAL-LIFE USAGE: An app loading your saved settings the millisecond you launch it.
        loaded_data = json.load(file)
        
        print(f"Welcome back, {loaded_data['username']}!")
        print(f"You have {len(loaded_data['inventory'])} items in your bag.")

except FileNotFoundError:
    print("[ERROR] No save file found. Starting a new game...")