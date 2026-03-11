# PROGRAM 3: THE JSON EXPORTER

# HOW: Imports the official JSON translation engine into Python.
# WHY: Python needs special tools to translate a live Dictionary into a text format the hard drive can store safely.
# REAL-LIFE USAGE: Exporting a database table into a backup file.
import json

# Here is a live dictionary in RAM. If we close the app now, it dies.
player_profile = {
    "username": "Rownak_KL",
    "level": 99,
    "inventory": ["Sword", "Shield", "Potion"]
}

# HOW: Open a file called 'save_game.json' in Write mode.
with open("save_game.json", "w") as file:
    
    # HOW: json.dump() takes the live dictionary (player_profile) and physically dumps it into the open file.
    # WHY: indent=4 formats the file with nice spacing so human eyes can read it easily.
    # REAL-LIFE USAGE: Saving a user's progress in a video game to their local hard drive.
    json.dump(player_profile, file, indent=4)

print("✅ SUCCESS: The player profile is permanently saved to 'save_game.json'.")