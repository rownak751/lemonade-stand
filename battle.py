# PROGRAM 3: THE MONSTER BATTLE GAME

# DATA STRUCTURE: A Dictionary linking the monster's name to its health points.
monsters = {"Goblin": 30, "Dragon": 100}

# FUNCTION: A sword attack that does math to lower the monster's health.
def swing_sword(monster_health, damage):
    return monster_health - damage

print("A wild monster appears!")

# WHILE LOOP: The battle keeps going until you run away.
while True:
    
    # FOR LOOP: Looking at all the monsters we can fight.
    print("\nMonsters you can fight:")
    for m in monsters:
        print(f"- {m} (Health: {monsters[m]})")
        
    choice = input("\nWho do you attack? (type 'run' to escape): ")
    
    # LOGIC: If they want to run, we stop the loop.
    if choice == "run":
        print("You ran away safely!")
        break
        
    if choice in monsters:
        try:
            # ERROR CATCHING: Make sure they swing the sword with a number.
            hit_power = int(input("How hard do you hit? (Enter a number 1-20): "))
            
            # LOGIC: You can't hit harder than 20!
            if hit_power > 20:
                print("Your sword isn't that strong! Try a smaller number.")
                continue # Skips to the top of the loop
                
            # MATH: We update the dictionary with the new health number.
            new_health = swing_sword(monsters[choice], hit_power)
            monsters[choice] = new_health
            
            if new_health <= 0:
                print(f"You defeated the {choice}!")
                # Remove the dead monster from the dictionary
                del monsters[choice]
            else:
                print(f"The {choice} is hurt! It has {new_health} health left.")
                
        except ValueError:
            print("You missed! You have to type a number to swing the sword.")
    else:
        print("There is no monster named that here.")