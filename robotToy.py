# PROGRAM 10: THE ROBOT TOY BUILDER

# DATA STRUCTURE: A list of robot parts you currently own.
my_parts = ["Head", "Arm", "Wheel"]

# FUNCTION: A scanner that checks if your robot has everything it needs to walk.
def can_robot_walk(parts_list):
    # LOGIC: It checks the list to see if the strings "Leg" or "Wheel" exist inside it.
    if "Leg" in parts_list or "Wheel" in parts_list:
        return True
    else:
        return False

print("Let's build a robot!")

# WHILE LOOP: Keep building until you turn the robot on.
while True:
    
    # FOR LOOP: Look inside your parts box and list what you have.
    print("\nYour Robot Currently Has:")
    for part in my_parts:
        print(f"- {part}")
        
    action = input("\nDo you want to 'add' a part or 'start' the robot? ")
    
    if action == "start":
        # We use our scanner function to test the robot.
        if can_robot_walk(my_parts):
            print("Beep Boop! The robot is moving! You win.")
        else:
            print("Crash! The robot has no legs or wheels to move. You need to add more parts.")
        break # Ends the game
        
    elif action == "add":
        try:
            # ERROR CATCHING: Ask them for a part name. We won't use math here, but we can catch blank inputs!
            new_part = input("Type the name of the new part: ")
            
            # MATH/LOGIC: We count the length of the word to make sure it's not blank.
            if len(new_part) == 0:
                # We "raise" our own error if they just hit Enter without typing.
                raise ValueError("You handed me invisible air!")
                
            my_parts.append(new_part)
            print("Part attached!")
            
        except ValueError as error_message:
            print(f"Oops: {error_message}")
    else:
        print("The factory doesn't understand that command.")