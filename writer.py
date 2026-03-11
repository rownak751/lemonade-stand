# PROGRAM 1: THE WRITER

# HOW: We use 'with open()' to open a portal to a file. 'w' stands for Write mode.
# WHY: 'with' automatically closes the file securely when the code finishes. 'w' creates the file if it doesn't exist.
# REAL-LIFE USAGE: Creating a raw log file to record server errors.
with open("my_notes.txt", "w") as file:
    
    # HOW: We push a string of text through the portal into the file.
    file.write("Hello from the matrix, Rownak.\n")
    file.write("This text will survive a computer reboot.")
    
print("✅ SUCCESS: Check your folder. 'my_notes.txt' has been created!")