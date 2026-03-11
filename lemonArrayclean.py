def is_valid_string(user_input):
    if user_input == "":
        print("[ERROR] Input cannot be empty.")
        return False
        
    try:
        float(user_input)
        print("[ERROR] Input cannot be a number. Please use words!")
        return False 
    except ValueError:
        return True 

def is_valid_number(user_input):
    if user_input == "":
        print("[ERROR] Number cannot be empty.")
        return False
        
    try:
        val = float(user_input)
        if val <= 0:
            print("[ERROR] Amount must be greater than RM 0.00!")
            return False
        return True 
    except ValueError:
        print("[ERROR] You must enter a valid number (like 2.50), not words!")
        return False 

def calculate_change(money_given, total_cost):
    return money_given - total_cost

menu = []

print("--- ADMIN MODE: BUILD YOUR MENU ---")

while True:
    new_flavor = input("\nEnter a flavor name (or type 'open' to open the stand): ").strip()
    
    if new_flavor.lower() == 'open':
        if len(menu) == 0:
            print("[ERROR] You must add at least one item to the menu first.")
            continue
        print("\nSaving database... Opening the stand to customers!\n")
        break
        
    if is_valid_string(new_flavor) == False:
        continue
    
    duplicate_found = False
    for item in menu:
        if item[0].lower() == new_flavor.lower():
            duplicate_found = True
            break
            
    if duplicate_found == True:
        print(f"[WARNING] '{new_flavor.title()}' is already on the menu! Please enter a different flavor.")
        continue

    while True:
        price_input = input(f"Enter the price for {new_flavor.title()}: RM ").strip()
        
        if is_valid_number(price_input) == False:
            continue
            
        new_price = float(price_input)
        break 

    menu.append([new_flavor.title(), new_price])
    print(f"✅ SUCCESS: {new_flavor.title()} added to the menu for RM {new_price:.2f}")

print("==========================================")
print("Welcome to the Lemonade Stand!")

while True:
    print("\nToday's Flavors:")
    for item in menu:
        print(f"- {item[0]}: RM {item[1]:.2f}")
        
    choice = input("\nWhat flavor do you want? (or type 'sleep' to close stand): ").strip().lower()
    
    if choice == "sleep":
        print("Closing the stand. Goodnight!")
        break

    if is_valid_string(choice) == False:
        continue
        
    selected_flavor = ""
    cost = 0.0
    
    for item in menu:
        if item[0].lower() == choice:
            selected_flavor = item[0]
            cost = item[1]
            break

    if selected_flavor != "":
        while True:
            money_string = input(f"\nHow much money for {selected_flavor}? RM ").strip()
            
            if is_valid_number(money_string) == False:
                continue
                
            money_float = float(money_string) 
            
            if money_float >= cost:
                change = calculate_change(money_float, cost)
                print(f"Here is your {selected_flavor} lemonade! Your change is RM {change:.2f}")
                break 
            else:
                print("Oops! You don't have enough money. Try again.")
                
    else:
        print("We don't have that flavor today.")