# PROGRAM 6: THE SPACESHIP DASHBOARD

# DATA STRUCTURE: Planets and how many miles away they are.
planets = {"Mars": 100, "Venus": 50, "Jupiter": 300}

# VARIABLES: Our ship's gas tank.
ship_fuel = 200.0

# FUNCTION: A navigation robot that checks if we have enough gas.
def can_we_reach_it(distance, fuel):
    if fuel >= distance:
        return True
    else:
        return False

# WHILE LOOP: We keep flying until we run out of gas or decide to land.
while True:
    print(f"\n--- DASHBOARD --- Fuel: {ship_fuel} gallons")
    
    # FOR LOOP: Looking at the star map to see where we can go.
    for p in planets:
        print(f"Planet {p} is {planets[p]} miles away.")
        
    destination = input("Where should we fly? (or 'land' to stop): ")
    
    # LOGIC: Stop flying if they want to land.
    if destination == "land":
        print("Landing ship. Welcome home!")
        break
        
    if destination in planets:
        try:
            # ERROR CATCHING: Making sure the pilot enters the speed correctly.
            speed = int(input("Enter warp speed (1, 2, or 3): "))
            
            distance_to_fly = planets[destination]
            
            # We use the robot function to check our gas tank.
            if can_we_reach_it(distance_to_fly, ship_fuel):
                # MATH: We burn the gas. Faster speed burns extra gas!
                ship_fuel = ship_fuel - (distance_to_fly + speed)
                print(f"Zoom! We arrived at {destination}.")
            else:
                print("Warning! Not enough fuel to go there.")
                
        except ValueError:
            print("Speed must be a number! The ship is confused.")
    else:
        print("That planet is not on the map.")