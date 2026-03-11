# PROGRAM 7: THE THEME PARK HEIGHT CHECKER

# DATA STRUCTURE: A dictionary of rollercoasters and how tall you must be to ride.
rides = {"Dragon Coaster": 48.0, "Teacup Spin": 36.0, "Tower Drop": 54.0}

# FUNCTION: A robot security guard measuring the kid.
def check_height(kid_height, ride_requirement):
    # MATH: Subtracting to see how many inches they are missing.
    difference = ride_requirement - kid_height
    return difference

print("Welcome to the Theme Park!")

# WHILE LOOP: The family keeps checking rides until they want to go home.
while True:
    
    # ERROR CATCHING: Getting the kid's height safely.
    try:
        height_input = input("\nHow tall is the child in inches? (or 'exit' to leave): ")
        
        # LOGIC: If they type exit, break the loop.
        if height_input == "exit":
            print("Thanks for visiting!")
            break
            
        child_height = float(height_input)
        
        # FOR LOOP: We check the child against EVERY ride in the park automatically.
        print("\n--- Ride Results ---")
        for ride_name in rides:
            required_height = rides[ride_name]
            
            # LOGIC: Are they tall enough?
            if child_height >= required_height:
                print(f"✅ Can ride: {ride_name}")
            else:
                # We use the math robot to see exactly how short they are.
                short_by = check_height(child_height, required_height)
                print(f"❌ Cannot ride: {ride_name} (Too short by {short_by} inches)")
                
    except ValueError:
        print("Please type a real number for the height!")