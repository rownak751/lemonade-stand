# HOW: Imports the official JavaScript Object Notation (JSON) library into Python.
# WHY: Python needs a translator to convert live Dictionaries and Arrays into safe text strings for the hard drive.
# REAL-LIFE USAGE: An iOS app communicating with a cloud server using JSON payloads to sync your data.
import json

# ==========================================
# --- THE 3 HELPER FUNCTIONS ---
# ==========================================

# HOW: Defines a reusable blueprint function named 'is_valid_string' that takes 'user_input'.
# WHY: Centralizes text-checking security logic so we don't rewrite it.
# REAL-LIFE USAGE: A backend validation script checking if a user's chosen password format is valid.
def is_valid_string(user_input):
    
    # HOW: Evaluates if 'user_input' is perfectly equal to an empty string ("").
    # WHY: Guards the database against blank entries which cause bugs.
    # REAL-LIFE USAGE: "Required Field" validation on a web form.
    if user_input == "":
        
        # HOW: Pushes a warning text to the terminal and returns the boolean 'False'.
        # WHY: Provides immediate feedback and flags the input as failed.
        # REAL-LIFE USAGE: The red text saying "Username cannot be blank" on a login screen.
        print("[ERROR] Input cannot be empty.")
        return False
        
    # HOW: Opens a protected sandbox where code can safely crash.
    # WHY: We are running a reverse-logic trap to catch numbers disguised as words.
    # REAL-LIFE USAGE: Fault-tolerant microservices catching unexpected API data types.
    try:
        
        # HOW: Attempts to convert the text into a decimal number.
        # WHY: If this succeeds, the user typed a number (like "5"), which we DO NOT want for a flavor name.
        # REAL-LIFE USAGE: Type-checking in databases to ensure names don't contain integers.
        float(user_input)
        
        # HOW: Prints an error and returns 'False'.
        # WHY: Explains the rule violation and rejects the data.
        # REAL-LIFE USAGE: Form validation telling a user "Name cannot contain numbers."
        print("[ERROR] Input cannot be a number. Please use words!")
        return False 
        
    # HOW: Intercepts the specific 'ValueError' crash caused by float() processing alphabet letters.
    # WHY: This crash proves the input is a real word. It is our success condition!
    # REAL-LIFE USAGE: Exception handling routing text data to the correct database column.
    except ValueError:
        
        # HOW: Returns 'True' back to the main program.
        # WHY: Confirms the input is safe, giving the main loop permission to proceed.
        # REAL-LIFE USAGE: A server authenticating a token and returning 'True' for access.
        return True 


# HOW: Defines a reusable function to validate money inputs.
# WHY: Centralizes our math-checking security logic.
# REAL-LIFE USAGE: A payment gateway ensuring a credit card charge is a valid number format.
def is_valid_number(user_input):
    
    # HOW: Evaluates if the variable is completely empty.
    # WHY: Math functions will violently crash if you feed them nothing.
    # REAL-LIFE USAGE: Preventing backend servers from crashing due to null data.
    if user_input == "":
        
        # HOW: Pushes warning and returns False.
        # WHY: Halts the transaction process due to missing data.
        # REAL-LIFE USAGE: Point of Sale (POS) system rejecting an empty cart.
        print("[ERROR] Number cannot be empty.")
        return False
        
    # HOW: Opens the protected sandbox for type conversion.
    # WHY: We are forcing raw human text to become computer math.
    # REAL-LIFE USAGE: Data sanitization in banking software.
    try:
        
        # HOW: Converts text into a decimal and locks it into variable 'val'.
        # WHY: We need a mathematical object to perform logic (like checking if it is greater than zero).
        # REAL-LIFE USAGE: Converting a string "$50.00" from a website input into a float 50.00.
        val = float(user_input)
        
        # HOW: Evaluates if 'val' is less than or equal to zero.
        # WHY: A core business logic rule: prices and payments must be positive.
        # REAL-LIFE USAGE: Anti-fraud logic preventing a hacker from transferring negative money.
        if val <= 0:
            
            # HOW: Prints warning and returns False.
            # WHY: The number is real, but it violates business rules.
            # REAL-LIFE USAGE: Warning a stock trader that they cannot buy 0 shares.
            print("[ERROR] Amount must be greater than RM 0.00!")
            return False
            
        # HOW: Returns True.
        # WHY: The data survived the crash test AND the negative test.
        # REAL-LIFE USAGE: A passing health check in a cloud server.
        return True 
        
    # HOW: Intercepts the ValueError if they typed letters instead of numbers.
    # WHY: Prevents the program from exploding.
    # REAL-LIFE USAGE: Catching bad user inputs in calculator apps.
    except ValueError:
        
        # HOW: Prints syntax guide and returns False.
        # WHY: Guides the user toward the correct format.
        # REAL-LIFE USAGE: A tooltip explaining "Please enter amounts in MM.DD format".
        print("[ERROR] You must enter a valid number (like 2.50), not words!")
        return False 


# HOW: Defines a function that subtracts 'total_cost' from 'money_given'.
# WHY: Isolates the core arithmetic into one safe place.
# REAL-LIFE USAGE: A dedicated "Compute Module" in an AWS Lambda function.
def calculate_change(money_given, total_cost):
    return money_given - total_cost


# ==========================================
# --- BOOTUP SEQUENCE 1: MENU DATABASE ---
# ==========================================

# HOW: Creates a completely empty dictionary {} in RAM.
# WHY: Initializes the data structure that will hold the application's menu state.
# REAL-LIFE USAGE: Instantiating a new memory cache before loading data into it.
menu = {}

# HOW: Opens a sandbox for the file-reading sequence.
# WHY: The first time you run this, "menu_database.json" doesn't exist. We must handle that gracefully.
# REAL-LIFE USAGE: A mobile app trying to load a user's local cache on first install.
try:
    
    # HOW: Creates a secure tunnel to "menu_database.json" in "r" (Read) mode using 'with'.
    # WHY: Read mode prevents accidental deletion. 'with' ensures the file closes automatically.
    # REAL-LIFE USAGE: A backend server reading a configuration file on startup.
    with open("menu_database.json", "r") as file:
        
        # HOW: Sucks the raw text out of the file and reconstructs it into the 'menu' Dictionary.
        # WHY: Converts dead hard-drive text back into live, searchable RAM.
        # REAL-LIFE USAGE: Loading a user's saved preferences from a local file.
        menu = json.load(file)
        
    # HOW: Pushes a success message to the terminal.
    # WHY: Confirms to the system admin that the historical data loaded safely.
    # REAL-LIFE USAGE: A server startup log showing "Database Connected Successfully."
    print("✅ MENU LOADED: Previous menu restored.")
    
# HOW: Intercepts the crash that happens when Python looks for a file that isn't there yet.
# WHY: Allows the program to survive the first-ever bootup.
# REAL-LIFE USAGE: Generating a default settings state if no save file is found.
except FileNotFoundError:
    print("⚠️ NO MENU FOUND: Starting with an empty menu.")


# ==========================================
# --- BOOTUP SEQUENCE 2: SALES LEDGER ---
# ==========================================

# HOW: Creates a completely empty Array [] in RAM.
# WHY: Initializes the chronological timeline structure that will hold all transaction objects.
# REAL-LIFE USAGE: Initializing an empty array before downloading transaction history from a bank API.
sales_history = []

# HOW: Opens the sandbox for the ledger file-reading sequence.
# WHY: Protects against the "File Not Found" crash on the very first sale.
# REAL-LIFE USAGE: Booting up an accounting software suite.
try:
    
    # HOW: Creates a secure tunnel to "sales_history.json" in "r" (Read) mode.
    # WHY: Accesses the permanent timeline of all past sales.
    # REAL-LIFE USAGE: Reading a server's permanent access logs.
    with open("sales_history.json", "r") as file:
        
        # HOW: Reconstructs the raw text into a live List of Dictionaries (Array of Objects).
        # WHY: Puts the historical timeline back into RAM so we can append new sales to the end of it.
        # REAL-LIFE USAGE: Loading a user's entire order history into the Amazon app.
        sales_history = json.load(file)
        
    # HOW: Pushes a success message, injecting the total count of past sales using len().
    # WHY: Gives the admin instant data visibility on bootup.
    # REAL-LIFE USAGE: A dashboard widget showing "Total Lifetime Orders: 54".
    print(f"✅ LEDGER LOADED: {len(sales_history)} previous sales found.")
    
except FileNotFoundError:
    # HOW: Warns the admin that the timeline is currently empty.
    # WHY: Expected behavior on day 1 of business.
    # REAL-LIFE USAGE: A message saying "You have not made any purchases yet."
    print("⚠️ NO LEDGER FOUND: Starting a fresh accounting book.")


# ==========================================
# --- PHASE 1: ADMIN DATABASE SETUP ---
# ==========================================

# HOW: Pushes a UI header to the terminal.
# WHY: Visually separates the bootup logs from the interactive Admin phase.
# REAL-LIFE USAGE: Rendering the top navigation bar of an admin dashboard.
print("\n--- ADMIN MODE: BUILD YOUR MENU ---")

# HOW: Starts an infinite loop.
# WHY: Keeps the Admin panel open indefinitely so they can add multiple items.
# REAL-LIFE USAGE: The main event loop of an operating system waiting for user input.
while True:
    
    # HOW: Pauses for input, strips blank spaces, and assigns to 'new_flavor'.
    # WHY: Standardizes raw input.
    # REAL-LIFE USAGE: Stripping spaces from an email address during account creation.
    new_flavor = input("\nEnter a flavor name (or type 'open' to open the stand): ").strip()
    
    # HOW: Temporarily squashes the input to lowercase and evaluates if it equals 'open'.
    # WHY: The administrative kill-switch to transition to Phase 2.
    # REAL-LIFE USAGE: A system admin typing 'start' into a bash terminal.
    if new_flavor.lower() == 'open':
        
        # HOW: Prevents a logical paradox. You cannot open a store with zero inventory.
        if len(menu) == 0:
            print("[ERROR] You must add at least one item to the menu first.")
            continue
            
        print("\nSaving database... Opening the stand to customers!\n")
        
        # HOW: Violently shatters the Admin loop.
        # WHY: Frees the program to move down into the Customer Phase.
        # REAL-LIFE USAGE: Breaking out of a setup wizard.
        break
        
    # HOW: Calls the string validator.
    # WHY: Guards the dictionary keys from corruption.
    # REAL-LIFE USAGE: Middleware checking authentication tokens.
    if is_valid_string(new_flavor) == False:
        continue
    
    # HOW: The Collision Radar. Evaluates if the capitalized string already exists in 'menu'.
    # WHY: Dictionaries overwrite duplicates; we must manually block them.
    # REAL-LIFE USAGE: Checking if an email is already registered.
    if new_flavor.title() in menu:
        print(f"[WARNING] '{new_flavor.title()}' is already on the menu! Please enter a different flavor.")
        continue

    # HOW: Starts a second, nested infinite loop.
    # WHY: Traps the admin in the pricing phase so we don't lose the validated 'new_flavor' variable.
    # REAL-LIFE USAGE: A multi-step checkout form.
    while True:
        
        # HOW: Pauses for input, assigns to 'price_input'.
        # WHY: Collects the dictionary value (the price).
        # REAL-LIFE USAGE: Dynamic HTML rendering for payment inputs.
        price_input = input(f"Enter the price for {new_flavor.title()}: RM ").strip()
        
        # HOW: Calls the number validator.
        # WHY: Guards the dictionary values.
        # REAL-LIFE USAGE: Validating a pricing update on a backend.
        if is_valid_number(price_input) == False:
            continue
            
        # HOW: Converts the validated string into a decimal.
        # WHY: Finalizes the data type for mathematical storage.
        # REAL-LIFE USAGE: Serializing data.
        new_price = float(price_input)
        
        # HOW: Shatters the nested price loop.
        # WHY: Both Key and Value are verified.
        # REAL-LIFE USAGE: Breaking out of a retry-loop.
        break 

    # HOW: Creates a new dictionary key and assigns the math float to it.
    # WHY: Permanently updates the live RAM application state.
    # REAL-LIFE USAGE: Executing an SQL 'INSERT INTO' command.
    menu[new_flavor.title()] = new_price
    
    print(f"✅ SUCCESS: {new_flavor.title()} added to the menu for RM {new_price:.2f}")

    # --- THE IMMORTALITY ENGINE (SAVE MENU TO HARD DRIVE) ---
    # HOW: Opens "menu_database.json" in Write mode and dumps the dictionary into it.
    # WHY: Protects the data against power failures by instantly committing to disk.
    # REAL-LIFE USAGE: Writing a configuration update to a permanent log.
    with open("menu_database.json", "w") as file:
        json.dump(menu, file, indent=4)


# ==========================================
# --- PHASE 2: CUSTOMER VIEW ---
# ==========================================

print("==========================================")
print("Welcome to the Lemonade Stand!")

# HOW: Starts the main operational loop.
# WHY: The server is "live".
# REAL-LIFE USAGE: A web server running continuously.
while True:
    
    print("\nToday's Flavors:")
    
    # HOW: Iterates through every key in the 'menu' dictionary and prints it.
    # WHY: Dynamically generates the UI.
    # REAL-LIFE USAGE: A frontend app mapping through an array of products.
    for flavor in menu:
        print(f"- {flavor}: RM {menu[flavor]:.2f}")
        
    # HOW: Pauses for input, standardizes to lowercase.
    # WHY: Prepares query for the search engine.
    # REAL-LIFE USAGE: Standardizing an Amazon search bar input.
    choice = input("\nWhat flavor do you want? (or type 'sleep' to close stand): ").strip().lower()
    
    # HOW: The master kill-switch.
    # WHY: Safely shuts down the server.
    # REAL-LIFE USAGE: Terminating a Docker container.
    if choice == "sleep":
        print("Closing the stand. Menu and Ledger safely saved. Goodnight!")
        break

    # HOW: Front-line security preventing bad queries.
    if is_valid_string(choice) == False:
        continue
        
    # HOW: Initializes temporary container for search results.
    selected_flavor = ""
    
    # HOW: The search engine algorithm. Matches input against dictionary keys.
    # WHY: Achieves case-insensitive matching.
    # REAL-LIFE USAGE: An 'ILIKE' database query.
    for flavor in menu:
        if flavor.lower() == choice:
            selected_flavor = flavor
            break

    # HOW: Evaluates if search was successful.
    if selected_flavor != "":
        
        # HOW: Locks user into payment phase.
        while True:
            money_string = input(f"\nHow much money for {selected_flavor}? RM ").strip()
            
            # HOW: Validates payment format.
            if is_valid_number(money_string) == False:
                continue
                
            # HOW: Converts text to math and pulls the exact cost from the dictionary.
            money_float = float(money_string) 
            cost = menu[selected_flavor]
            
            # HOW: Core transactional logic. Checks for sufficient funds.
            if money_float >= cost:
                
                # HOW: Executes transaction math.
                change = calculate_change(money_float, cost)
                print(f"Here is your {selected_flavor} lemonade! Your change is RM {change:.2f}")
                
                # ==========================================
                # --- NEW LEDGER RECORDING SYSTEM ---
                # ==========================================
                
                # HOW: Counts the length of the current sales array and adds 1.
                # WHY: Dynamically generates the next logical Customer ID regardless of how many days the program has been running.
                # REAL-LIFE USAGE: Auto-incrementing a Primary Key (ID) in an SQL database table.
                customer_number = len(sales_history) + 1
                
                # HOW: Creates a single Dictionary grouping all specific transaction details.
                # WHY: Constructs the "Object" part of our "Array of Objects" architecture. Labels the math clearly.
                # REAL-LIFE USAGE: Generating a JSON payload representing a single e-commerce checkout.
                transaction_receipt = {
                    "customer": f"Customer {customer_number}",
                    "item_sold": selected_flavor,
                    "cost": cost,
                    "money_given": money_float,
                    "change_returned": change
                }
                
                # HOW: Injects the new Dictionary into the main chronological Array.
                # WHY: Updates the live RAM timeline of sales.
                # REAL-LIFE USAGE: Pushing a new block to a blockchain ledger.
                sales_history.append(transaction_receipt)
                
                # HOW: Opens "sales_history.json" in Write mode and completely overwrites it with the updated array.
                # WHY: The Ledger Immortality Engine. Instantly commits the transaction to the hard drive so the receipt is never lost.
                # REAL-LIFE USAGE: A bank logging a wire transfer permanently to a server farm.
                with open("sales_history.json", "w") as file:
                    json.dump(sales_history, file, indent=4)
                    
                # HOW: Pushes a quiet confirmation to the terminal.
                # WHY: System-level feedback that the ledger update succeeded.
                # REAL-LIFE USAGE: A terminal log saying "200 OK: POST /api/transactions"
                print(f"🧾 [System] Transaction logged for Customer {customer_number}.")
                
                # ==========================================
                
                # HOW: Shatters transaction loop, releasing customer.
                break 
                
            else:
                # HOW: Handles failed transaction.
                print("Oops! You don't have enough money. Try again.")
                
    else:
        # HOW: Handles 404 Not Found.
        print("We don't have that flavor today.")