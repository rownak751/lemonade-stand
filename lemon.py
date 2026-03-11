# PROGRAM 1: THE LEMONADE STAND (THE ULTRA-ATOMIC EDITION)

# ==========================================
# --- THE 3 HELPER FUNCTIONS ---
# ==========================================

def is_valid_string(user_input):
    
    # HOW: Evaluates if the variable 'user_input' is completely empty (no characters).
    # WHY: A blank string will corrupt the dictionary and provides no useful data.
    # REAL-LIFE USAGE: "Required Field" validation on a web form (e.g., preventing a user from leaving 'First Name' blank).
    if user_input == "":
        
        # HOW: Pushes a warning text string to the user's screen.
        # WHY: The user needs immediate, actionable feedback so they know what they did wrong.
        # REAL-LIFE USAGE: UI/UX error messaging (the red text that appears under an invalid password box).
        print("[ERROR] Input cannot be empty.")
        
        # HOW: Instantly terminates the function and passes the boolean value 'False' back.
        # WHY: We must flag the data as "failed" so the main loop knows to reject it.
        # REAL-LIFE USAGE: HTTP 400 Bad Request. A server rejecting a bad payload and sending a 'Failed' signal back to the browser.
        return False
        
    # HOW: Opens a protected sandbox where code can safely crash without taking down the server.
    # WHY: We are about to run a dangerous math conversion that we EXPECT to fail sometimes.
    # REAL-LIFE USAGE: Fault-tolerant microservices. If a payment gateway goes down, a try/except block catches the crash so the rest of the website stays online.
    try:
        
        # HOW: Attempts to mathematically convert the text variable into a decimal number.
        # WHY: This is a reverse-logic trap. If it succeeds, the user typed a number, which we DO NOT want for a text name.
        # REAL-LIFE USAGE: Type-checking in databases. Ensuring a 'Username' column isn't accidentally filled with raw integers.
        float(user_input)
        
        # HOW: Prints an error because the reverse-trap succeeded (it was a number).
        # WHY: Explains the specific rule violation to the user.
        # REAL-LIFE USAGE: Form validation telling a user "Name cannot contain numbers."
        print("[ERROR] Input cannot be a number. Please use words!")
        
        # HOW: Terminates the function and passes 'False' back.
        # WHY: The input failed the "must be text" security test.
        # REAL-LIFE USAGE: Failing an automated unit test in a CI/CD pipeline because the data format is wrong.
        return False 
        
    # HOW: Intercepts the specific 'ValueError' crash caused by float() trying to process alphabet letters.
    # WHY: This crash is actually our success condition! It proves the input is a real word.
    # REAL-LIFE USAGE: Exception handling in Data Engineering pipelines to route non-numerical data into the correct text-processing queue.
    except ValueError:
        
        # HOW: Terminates the function and passes 'True' back.
        # WHY: Confirms the input is safe, valid text, giving the main loop permission to proceed.
        # REAL-LIFE USAGE: A JWT (JSON Web Token) successfully authenticating a user and returning 'True' for access.
        return True 


def is_valid_number(user_input):
    
    # HOW: Evaluates if the variable is completely empty.
    # WHY: Math functions will violently crash if you feed them nothing.
    # REAL-LIFE USAGE: Preventing null-pointer exceptions in backend Java or C++ servers.
    if user_input == "":
        
        # HOW: Pushes the warning to the screen.
        # WHY: Immediate user correction.
        # REAL-LIFE USAGE: Prompting a cashier that they forgot to enter the cash amount before hitting Enter.
        print("[ERROR] Number cannot be empty.")
        
        # HOW: Terminates and returns False.
        # WHY: Halts the transaction process.
        # REAL-LIFE USAGE: A declined transaction flag at a Point of Sale (POS) system.
        return False
        
    # HOW: Opens the protected sandbox.
    # WHY: We are taking raw human text and forcing it to become computer math.
    # REAL-LIFE USAGE: Data sanitization gateways in Fintech applications.
    try:
        
        # HOW: Converts the text into a decimal and locks it into variable 'val'.
        # WHY: We need a mathematical object to perform logical comparisons (like greater than/less than).
        # REAL-LIFE USAGE: Converting a string "$50.00" from a website input field into a float 50.00 for the database.
        val = float(user_input)
        
        # HOW: Evaluates if 'val' is less than or equal to zero.
        # WHY: A core business logic rule: prices and payments must be positive.
        # REAL-LIFE USAGE: Anti-fraud logic. Preventing a hacker from transferring "-$1000" to steal money from a bank API.
        if val <= 0:
            
            # HOW: Pushes the specific math warning to the screen.
            # WHY: Explains exactly why the number was rejected.
            # REAL-LIFE USAGE: Warning a stock trader that they cannot buy 0 shares.
            print("[ERROR] Amount must be greater than RM 0.00!")
            
            # HOW: Terminates and returns False.
            # WHY: The number is real, but it violates business rules.
            # REAL-LIFE USAGE: A server rejecting a trade order due to invalid parameters.
            return False
            
        # HOW: Terminates and returns True.
        # WHY: The data survived the crash test AND the negative test. It is pure.
        # REAL-LIFE USAGE: A passing health check in a cloud server, greenlighting the deployment.
        return True 
        
    # HOW: Intercepts the ValueError if they typed alphabet letters.
    # WHY: Prevents the program from exploding if a user types "Five" instead of "5".
    # REAL-LIFE USAGE: Catching bad user inputs in calculator apps or spreadsheet cells.
    except ValueError:
        
        # HOW: Explains how to format the number.
        # WHY: Guides the user toward the correct syntax.
        # REAL-LIFE USAGE: A tooltip explaining "Please enter amounts in MM.DD format".
        print("[ERROR] You must enter a valid number (like 2.50), not words!")
        
        # HOW: Terminates and returns False.
        # WHY: The input is corrupted.
        # REAL-LIFE USAGE: Bouncing a corrupted packet in network routing.
        return False 


def calculate_change(money_given, total_cost):
    
    # HOW: Subtracts 'total_cost' from 'money_given', and instantly spits the result out.
    # WHY: Centralizes the core arithmetic of the application. 
    # REAL-LIFE USAGE: A dedicated "Compute Module" in an AWS serverless Lambda function that only spins up to do math and shut down.
    return money_given - total_cost


# ==========================================
# --- PHASE 1: ADMIN DATABASE SETUP ---
# ==========================================

# HOW: Creates a completely empty dictionary {} in RAM.
# WHY: Initializes the data structure that will hold the state of the application.
# REAL-LIFE USAGE: Instantiating a new, blank MongoDB document or Redis cache instance.
menu = {}

print("--- ADMIN MODE: BUILD YOUR MENU ---")

# HOW: Starts an infinite loop (while True).
# WHY: Keeps the Admin panel open indefinitely so they can add as many items as they want.
# REAL-LIFE USAGE: The main event loop of an operating system or a video game engine waiting for user actions.
while True:
    
    # HOW: Pauses for input, cuts off blank spaces with .strip(), and assigns to 'new_flavor'.
    # WHY: Standardizes the raw input before it hits our security checks.
    # REAL-LIFE USAGE: Stripping trailing spaces from an email address during account creation so the login doesn't fail later.
    new_flavor = input("\nEnter a flavor name (or type 'open' to open the stand): ").strip()
    
    # HOW: Temporarily squashes the input to lowercase and checks if it equals 'open'.
    # WHY: The administrative command to transition from Phase 1 to Phase 2.
    # REAL-LIFE USAGE: A system administrator typing 'exit' or 'start' into a Linux bash terminal to trigger a state change.
    if new_flavor.lower() == 'open':
        
        # HOW: Counts the items in the dictionary. Checks if count is 0.
        # WHY: Prevents a logical paradox. You cannot run a store with zero inventory.
        # REAL-LIFE USAGE: Preventing a webmaster from publishing a blog post that has no title or content.
        if len(menu) == 0:
            
            # HOW: Pushes a warning to the screen.
            # WHY: Informs the admin they missed a prerequisite step.
            # REAL-LIFE USAGE: "You must add at least one product to your Shopify store before going live."
            print("[ERROR] You must add at least one item to the menu first.")
            
            # HOW: Instantly forces the 'while True' loop to skip the rest of the code and jump back to the top.
            # WHY: Acts as a hard stop, resetting the admin's action without crashing the program.
            # REAL-LIFE USAGE: A loop continuing to listen for incoming connections after rejecting a bad IP address.
            continue
            
        print("\nSaving database... Opening the stand to customers!\n")
        
        # HOW: Violently shatters the current 'while True' loop.
        # WHY: Frees the program to move down the script into the Customer Phase.
        # REAL-LIFE USAGE: Breaking out of a setup wizard once the user clicks "Finish".
        break
        
    # HOW: Calls the string validator, hands it 'new_flavor', and evaluates if it equals 'False'.
    # WHY: The first security checkpoint. Guards the dictionary keys from corruption.
    # REAL-LIFE USAGE: A middleware layer in a Node.js server checking authentication tokens before allowing database access.
    if is_valid_string(new_flavor) == False:
        
        # HOW: Forces the loop to restart.
        # WHY: The data failed security; discard it and demand new data.
        # REAL-LIFE USAGE: Refreshing a captcha because the user failed the security check.
        continue

# --- NEW SECURITY CHECKPOINT: THE DUPLICATE RADAR ---
    
    # HOW: Evaluates if the perfectly capitalized new flavor already exists as a key inside the 'menu' dictionary.
    # WHY: Dictionaries cannot hold two identical keys. If we let the admin proceed, the old price will be silently overwritten. We block it entirely.
    # REAL-LIFE USAGE: Preventing a user from creating a new account with an email address that is already registered in the database.
    if new_flavor.title() in menu:
        
        # HOW: Pushes a specific warning alerting the admin that the item already exists.
        # WHY: Gives immediate feedback so they know exactly why their input was rejected.
        # REAL-LIFE USAGE: A pop-up saying "Username already taken, please choose another."
        print(f"[WARNING] '{new_flavor.title()}' is already on the menu! Please enter a different flavor.")
        
        # HOW: Forces the main loop to restart.
        # WHY: Rejects the duplicate entry and instantly asks for a brand new flavor name.
        # REAL-LIFE USAGE: Stopping the SQL database INSERT command and refreshing the signup form.
        continue

    # ----------------------------------------------------

    # HOW: Starts a second, nested infinite loop.
    # WHY: We secured the flavor name; we don't want to lose it. We trap the user here until they get the price right.
    # REAL-LIFE USAGE: A multi-step checkout form. You don't make the user re-enter their shipping address if their credit card fails.
    while True:
        
        # HOW: Uses an f-string to inject the capitalized name into the prompt.
        # WHY: Dynamic UI feedback to confirm to the user exactly what item they are pricing.
        # REAL-LIFE USAGE: Dynamic HTML rendering (like React or Vue.js) updating a page to say "Enter payment for your MacBook Pro".
        price_input = input(f"Enter the price for {new_flavor.title()}: RM ").strip()
        
        # HOW: Calls the number validator, evaluates if it equals 'False'.
        # WHY: The second security checkpoint. Guards the dictionary values from corruption.
        # REAL-LIFE USAGE: Validating a pricing update on an e-commerce backend portal.
        if is_valid_number(price_input) == False:
            
            # HOW: Forces the nested price loop to restart.
            # WHY: Discards the bad price without losing the 'new_flavor' variable.
            # REAL-LIFE USAGE: Clearing just the 'Credit Card Number' field on a form while leaving the rest intact.
            continue
            
        # HOW: Converts the verified text into a decimal number.
        # WHY: Locks the data into its final mathematical format for storage.
        # REAL-LIFE USAGE: Serializing data before writing it to a hard drive.
        new_price = float(price_input)
        
        # HOW: Shatters the nested price loop.
        # WHY: The price is verified. We are ready to commit to the database.
        # REAL-LIFE USAGE: Breaking out of a retry-loop once an API successfully connects.
        break 

    # HOW: Creates a new drawer using the capitalized name as the label, and locks the math number inside it.
    # WHY: Permanently updates the application state. The item now officially exists.
    # REAL-LIFE USAGE: An SQL 'INSERT INTO menu (item, price) VALUES (...)' command executing in a live database.
    menu[new_flavor.title()] = new_price
    
    print(f"✅ SUCCESS: {new_flavor.title()} added to the menu for RM {new_price:.2f}")


# ==========================================
# --- PHASE 2: CUSTOMER VIEW ---
# ==========================================

print("==========================================")
print("Welcome to the Lemonade Stand!")

# HOW: Starts the main, infinite operational loop.
# WHY: The server is now "live" and listening for continuous customer requests.
# REAL-LIFE USAGE: An NGINX or Apache web server running continuously to serve millions of HTTP requests.
while True:
    
    print("\nToday's Flavors:")
    
    # HOW: Iterates through the keys of the dictionary.
    # WHY: Dynamically generates the UI based on the current state of the database.
    # REAL-LIFE USAGE: A frontend app fetching an array of products via an API and rendering them on screen using a map() function.
    for flavor in menu:
        
        # HOW: Prints the key and reaches into the dictionary to pull out the matching value, formatting to 2 decimals.
        # WHY: Presents the data cleanly to the end user.
        # REAL-LIFE USAGE: Displaying "Product Name: $Price" on an Amazon search page.
        print(f"- {flavor}: RM {menu[flavor]:.2f}")
        
    # HOW: Pauses for input, strips spaces, and permanently crushes it to lowercase.
    # WHY: Standardizes the user's messy input into a predictable format for searching.
    # REAL-LIFE USAGE: A search engine standardizing a user's query before looking it up in the index.
    choice = input("\nWhat flavor do you want? (or type 'sleep' to close stand): ").strip().lower()
    
    # HOW: Evaluates if 'choice' matches the shutdown command.
    # WHY: The master kill-switch for the application.
    # REAL-LIFE USAGE: Sending a SIGTERM (Terminate Signal) to safely shut down a running Docker container.
    if choice == "sleep":
        
        print("Closing the stand. Goodnight!")
        
        # HOW: Shatters the main operational loop.
        # WHY: Allows the script to reach the end of the file, clearing it from the computer's RAM.
        # REAL-LIFE USAGE: A server gracefully shutting down after finishing its current tasks.
        break

    # HOW: Calls the string validator.
    # WHY: Front-line security preventing bad queries from hitting our search algorithm.
    # REAL-LIFE USAGE: Preventing SQL Injection attacks by catching weird symbols before they reach the database.
    if is_valid_string(choice) == False:
        
        # HOW: Forces the loop to restart.
        # WHY: The query is invalid. Reject it.
        # REAL-LIFE USAGE: A 400 Bad Request error.
        continue
        
    # HOW: Creates an empty string variable.
    # WHY: Initializes a temporary container to hold the result of our database search.
    # REAL-LIFE USAGE: Creating an empty 'results' array before querying an SQL database.
    selected_flavor = ""
    
    # HOW: Starts a loop looking at every key label in the dictionary.
    # WHY: The actual search engine algorithm.
    # REAL-LIFE USAGE: A linear search algorithm scanning through a list of active users.
    for flavor in menu:
        
        # HOW: Temporarily squashes the dictionary label to lowercase to see if it perfectly matches the customer's input.
        # WHY: Achieves case-insensitive matching without destroying the original capitalized data.
        # REAL-LIFE USAGE: An 'ILIKE' command in PostgreSQL for case-insensitive querying.
        if flavor.lower() == choice:
            
            # HOW: Takes the original, correctly capitalized dictionary label and locks it into our holding container.
            # WHY: We successfully found the target! We save the "True" spelling for later use.
            # REAL-LIFE USAGE: Saving the exact database Row ID after finding a match.
            selected_flavor = flavor
            
            # HOW: Shatters the 'for' loop early.
            # WHY: Optimization. We found the match, so it is a waste of CPU power to keep checking the rest of the dictionary.
            # REAL-LIFE USAGE: Algorithmic efficiency (Big O Notation). Stopping a search immediately to save compute time.
            break

    # HOW: Evaluates if our holding container caught a matching label (!= "").
    # WHY: Checks if the search engine algorithm was successful.
    # REAL-LIFE USAGE: Checking if a database query returned 'null' or actual data.
    if selected_flavor != "":
        
        # HOW: Starts a nested transaction loop.
        # WHY: Locks the user into the payment phase for the specific item they selected.
        # REAL-LIFE USAGE: Redirecting a user to a secure Stripe payment gateway page.
        while True:
            
            money_string = input(f"\nHow much money for {selected_flavor}? RM ").strip()
            
            # HOW: Calls the number validator.
            # WHY: Security checkpoint to ensure payment data is mathematically sound.
            # REAL-LIFE USAGE: Validating a credit card number format before sending it to Visa.
            if is_valid_number(money_string) == False:
                
                # HOW: Forces the payment loop to restart.
                # WHY: Reject bad payment format without losing the user's cart.
                # REAL-LIFE USAGE: Highlighting the CC field red but keeping the item in the cart.
                continue
                
            # HOW: Converts text to math.
            # WHY: Prepares for arithmetic logic.
            # REAL-LIFE USAGE: Casting string inputs to integers in a banking app.
            money_float = float(money_string) 
            
            # HOW: Pulls the exact price using the verified key.
            # WHY: Retrieves the source of truth for the price, rather than trusting the client.
            # REAL-LIFE USAGE: Fetching the price from the backend server instead of trusting the price shown in the user's browser (which can be hacked).
            cost = menu[selected_flavor]
            
            # HOW: Evaluates if money is >= cost.
            # WHY: Core transactional logic.
            # REAL-LIFE USAGE: Bank authorization checking if you have sufficient funds.
            if money_float >= cost:
                
                # HOW: Passes variables to calculator, saves to 'change'.
                # WHY: Executes the business transaction.
                # REAL-LIFE USAGE: Triggering the final ledger update in a FinTech system.
                change = calculate_change(money_float, cost)
                
                print(f"Here is your {selected_flavor} lemonade! Your change is RM {change:.2f}")
                
                # HOW: Shatters the nested transaction loop.
                # WHY: Sale is complete. Release the customer and prepare for the next one.
                # REAL-LIFE USAGE: Returning a 200 OK status and closing the HTTP connection.
                break 
                
            # HOW: Executes if money is less than cost.
            # WHY: Handles the failure state of the business logic.
            # REAL-LIFE USAGE: Displaying "Insufficient Funds" on an ATM.
            else:
                print("Oops! You don't have enough money. Try again.")
                
    # HOW: Executes if the search engine loop found zero matches.
    # WHY: Handles the 404 Not Found state.
    # REAL-LIFE USAGE: Returning a 404 Error page when a user searches for a deleted product.
    else:
        print("We don't have that flavor today.")