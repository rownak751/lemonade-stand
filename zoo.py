# PROGRAM 2: THE ZOO ANIMAL FEEDER (UPGRADED VERSION)

# HOW: We use square brackets [] to create a List. It holds multiple Strings separated by commas.
# WHY: We need a line of animals waiting to be fed. Unlike a Dictionary, a List keeps things in an exact, ordered sequence.
# AI/ML CONTEXT: In Machine Learning, Lists (and their advanced cousins, NumPy Arrays or Tensors) are the lifeblood of data. 
# You will use Lists to hold thousands of image file paths or to store the history of your model's accuracy scores over time.
hungry_animals = ["Lion", "Monkey", "Elephant"]

# HOW: 'def' creates a function that takes one input (food_amount). It uses an 'if/else' check to return a Boolean (True or False).
# WHY: We need a dedicated sensor to constantly monitor the food supply. By making it a function, we keep the main code clean.
# AI/ML CONTEXT: This is exactly how "Early Stopping" works in AI training. You write a function that constantly checks the model's error rate. 
# If the error rate stops improving (hits 0), the function returns False, and the training loop safely shuts down to save computing power.
def check_food_bucket(food_amount):
    if food_amount <= 0:
        return False # The bucket is empty!
    else:
        return True # We still have food!

# HOW: Creates a standard Float variable.
bucket_weight = 10.0 

# HOW: len() counts how many items are currently inside the list. 'while len > 0:' tells the loop to keep running as long as the list is not empty.
# WHY: We don't want an infinite 'while True' loop here. 
# The job has a clear finish line: the program should naturally shut down the exact second the last animal is fed.
while len(hungry_animals) > 0:
    
    print("\nAnimals waiting for food:")
    
    for animal in hungry_animals:
        print(f"- {animal}")
        
    # --- UPGRADED SCANNER INTEGRATION STARTS HERE ---
    
    # HOW: We grab the user's text and instantly crush it into lowercase.
    # WHY: Data sanitization. We force messy human input ("LiON") into a predictable format ("lion").
    user_target = input("\nWhich animal do you want to feed? ").lower()
    
    # HOW: Creates a blank string to act as a temporary holding box.
    selected_animal = ""
    
    # HOW: The scanner loop looks at the master list one by one.
    for animal in hungry_animals:
        # HOW: animal.lower() temporarily makes the master list item lowercase to see if it perfectly matches the user's lowercase input.
        if animal.lower() == user_target:
            # HOW: If it matches, we save the TRUE capitalized name ("Lion") into our holding box.
            selected_animal = animal
            break # Shatters the mini-loop because we found our match.

    # HOW: Instead of checking 'if target in hungry_animals', we just check if our holding box caught something.
    # WHY: If selected_animal is NOT empty (!= ""), it means our scanner successfully verified the animal exists.
    if selected_animal != "":
        
    # --- UPGRADED SCANNER INTEGRATION ENDS HERE ---

        # HOW: 'try:' opens the safety net for dangerous user input.
        try:
            
            # HOW: Grabs input and instantly crushes it into a decimal number using float().
            # NOTICE: We use selected_animal here so it prints the properly capitalized name.
            amount_to_feed = float(input(f"How many pounds of food for the {selected_animal}? "))
            
            # HOW: Takes the current weight, subtracts the food eaten, and permanently saves that new lower number back into the bucket_weight variable.
            bucket_weight = bucket_weight - amount_to_feed
            
            # HOW: Calls our sensor function and hands it the brand new bucket_weight. If it returns False, the bucket is empty.
            if check_food_bucket(bucket_weight) == False:
                print("Oh no! The bucket is empty! We have to stop feeding.")
                # HOW: 'break' violently shatters the main while loop, ending the program.
                break
                
            else:
                print(f"Yum! The {selected_animal} ate it. We have {bucket_weight} pounds of food left.")
                
                # HOW: The .remove() command targets the specific item in the list and deletes it forever. 
                # WHY: The animal is full. If we don't remove it, the loop will think it still needs to be fed.
                hungry_animals.remove(selected_animal)
                
        # HOW: Catches the exact crash that happens if float() tries to process alphabet letters.
        except ValueError:
            print("Please type a number. You can't feed an animal alphabet letters!")
            
    else:
        # HOW: Runs if selected_animal is still equal to "", meaning the scanner loop found absolutely nothing.
        print("That animal is not in this zoo!")
        
# HOW: This print statement is pushed all the way to the left (un-indented). 
# WHY: It exists completely outside the while loop. It will only ever print once the loop is fully destroyed.
print("Zoo feeding time is over!")