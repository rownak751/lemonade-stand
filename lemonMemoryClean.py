import json

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


# ==========================================
# --- BOOTUP SEQUENCE 1: MENU DATABASE ---
# ==========================================
menu = {}
try:
    with open("menu_database.json", "r") as file:
        menu = json.load(file)
    print("✅ MENU LOADED: Previous menu restored.")
except FileNotFoundError:
    print("⚠️ NO MENU FOUND: Starting with an empty menu.")


# ==========================================
# --- BOOTUP SEQUENCE 2: SALES LEDGER ---
# ==========================================

# HOW: Initializes an empty Array/List to hold our hybrid transaction logs.
sales_history = []

try:
    # HOW: Tries to load the continuous timeline of past sales.
    with open("sales_history.json", "r") as file:
        sales_history = json.load(file)
    print(f"✅ LEDGER LOADED: {len(sales_history)} previous sales found.")
except FileNotFoundError:
    print("⚠️ NO LEDGER FOUND: Starting a fresh accounting book.")


# ==========================================
# --- PHASE 1: ADMIN DATABASE SETUP ---
# ==========================================
print("\n--- ADMIN MODE: BUILD YOUR MENU ---")

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
    
    if new_flavor.title() in menu:
        print(f"[WARNING] '{new_flavor.title()}' is already on the menu! Please enter a different flavor.")
        continue

    while True:
        price_input = input(f"Enter the price for {new_flavor.title()}: RM ").strip()
        if is_valid_number(price_input) == False:
            continue
        new_price = float(price_input)
        break 

    menu[new_flavor.title()] = new_price
    print(f"✅ SUCCESS: {new_flavor.title()} added to the menu for RM {new_price:.2f}")

    with open("menu_database.json", "w") as file:
        json.dump(menu, file, indent=4)


# ==========================================
# --- PHASE 2: CUSTOMER VIEW ---
# ==========================================
print("==========================================")
print("Welcome to the Lemonade Stand!")

while True:
    print("\nToday's Flavors:")
    for flavor in menu:
        print(f"- {flavor}: RM {menu[flavor]:.2f}")
        
    choice = input("\nWhat flavor do you want? (or type 'sleep' to close stand): ").strip().lower()
    
    if choice == "sleep":
        print("Closing the stand. Menu and Ledger safely saved. Goodnight!")
        break

    if is_valid_string(choice) == False:
        continue
        
    selected_flavor = ""
    for flavor in menu:
        if flavor.lower() == choice:
            selected_flavor = flavor
            break

    if selected_flavor != "":
        while True:
            money_string = input(f"\nHow much money for {selected_flavor}? RM ").strip()
            
            if is_valid_number(money_string) == False:
                continue
                
            money_float = float(money_string) 
            cost = menu[selected_flavor]
            
            if money_float >= cost:
                change = calculate_change(money_float, cost)
                print(f"Here is your {selected_flavor} lemonade! Your change is RM {change:.2f}")
                
                # ==========================================
                # --- NEW LEDGER RECORDING SYSTEM ---
                # ==========================================
                
                # HOW: Counts how many items are already in the array, and adds 1 to figure out the next customer number.
                # WHY: If there are 2 items saved from yesterday, len() is 2. 2 + 1 = 3. This person is Customer 3.
                customer_number = len(sales_history) + 1
                
                # HOW: Creates a dictionary holding all the exact transaction details with clear labels.
                transaction_receipt = {
                    "customer": f"Customer {customer_number}",
                    "item_sold": selected_flavor,
                    "cost": cost,
                    "money_given": money_float,
                    "change_returned": change
                }
                
                # HOW: Pushes this dictionary into the master tracking array.
                sales_history.append(transaction_receipt)
                
                # HOW: Instantly writes the updated array to a separate JSON file.
                # WHY: Your sales data is just as critical as your menu data. We commit it to disk immediately so you never lose a receipt.
                with open("sales_history.json", "w") as file:
                    json.dump(sales_history, file, indent=4)
                    
                print(f"🧾 [System] Transaction logged for Customer {customer_number}.")
                # ==========================================
                
                break 
            else:
                print("Oops! You don't have enough money. Try again.")
                
    else:
        print("We don't have that flavor today.")