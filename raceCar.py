# PROGRAM 9: THE RACE CAR PIT STOP

# DATA STRUCTURE: Cars and the health of their tires (100 is perfect).
cars = {"Red Car": 100, "Blue Car": 40, "Green Car": 10}

# FUNCTION: A mechanic robot that fixes tires back to 100.
def fix_tires(current_health):
    # MATH: Find out how much health is missing to make it exactly 100 again.
    missing_health = 100 - current_health
    return missing_health

print("Welcome to the Pit Stop!")

# WHILE LOOP: The race continues until all cars are fixed or you quit.
while True:
    
    # FOR LOOP: Show the mechanic the health of all the cars.
    print("\n--- Race Status ---")
    for car in cars:
        print(f"{car}: Tire Health {cars[car]}")
        
    choice = input("\nWhich car needs to be fixed? (or 'quit' to end race): ")
    
    # LOGIC: Stop the race if they type quit.
    if choice == "quit":
        break
        
    if choice in cars:
        try:
            # ERROR CATCHING: How many mechanics are working on the car?
            workers = int(input("How many mechanics will work on this? (1-5): "))
            
            # LOGIC: If you have enough workers, the car gets fixed perfectly.
            if workers > 0:
                amount_fixed = fix_tires(cars[choice])
                cars[choice] = cars[choice] + amount_fixed
                print(f"Vroom! {choice} tires are back to 100 health.")
            else:
                print("You need at least 1 mechanic to fix a car!")
                
        except ValueError:
            print("Mechanics must be counted in whole numbers!")
    else:
        print("That car is not on the track.")