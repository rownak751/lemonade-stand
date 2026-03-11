# PROGRAM 4: THE MAGIC BACKPACK

# DATA STRUCTURE: An empty List, like a backpack with nothing inside it yet.
backpack = []

# VARIABLES: The backpack can only hold 50 pounds total.
MAX_WEIGHT = 50.0

# FUNCTION: A tiny robot that adds up all the weight currently in the backpack.
def get_total_weight(current_items):
    total = 0
    # FOR LOOP: It pulls out every item, looks at its weight, and adds it up.
    for item in current_items:
        total = total + item['weight']
    return total

print("Let's pack for the adventure!")

# WHILE LOOP: We keep packing until we say 'done'.
while True:
    thing = input("\nWhat are you putting in the backpack? (or 'done'): ")
    
    # LOGIC: Stop packing if they type done.
    if thing == "done":
        break
        
    try:
        # ERROR CATCHING: Make sure the weight is a real number.
        weight_input = float(input(f"How heavy is the {thing} in pounds? "))
        
        # We build a mini dictionary for this one item and pretend it's a toy box.
        new_toy_box = {"name": thing, "weight": weight_input}
        
        # We throw the toy box into the backpack list temporarily to test it.
        backpack.append(new_toy_box)
        
        # MATH: We use the robot function to check the new total weight.
        current_weight = get_total_weight(backpack)
        
        # LOGIC: Did adding that item make the backpack too heavy?
        if current_weight > MAX_WEIGHT:
            print("Too heavy! The backpack ripped! We have to take that out.")
            # It's too heavy, so we remove the item we just added.
            backpack.pop() 
        else:
            print(f"Packed! Backpack weighs {current_weight} pounds now.")
            
    except ValueError:
        print("Weight has to be a number!")

print(f"\nYou packed {len(backpack)} items. Time to go!")