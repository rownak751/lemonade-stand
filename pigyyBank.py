# PROGRAM 8: THE SECRET PIGGY BANK

# DATA STRUCTURE: A list of coins currently inside the piggy bank.
coins_inside = [1.0, 5.0, 0.5] 

# FUNCTION: A robot that smashes the bank open and counts the money.
def count_money(coin_list):
    total = 0
    # FOR LOOP: Grabs every coin and adds it to the total.
    for coin in coin_list:
        total = total + coin
    return total

print("This is your secret digital piggy bank.")

# WHILE LOOP: Keep adding money until you want to smash it open.
while True:
    action = input("\nDo you want to 'add' a coin, or 'smash' the bank? ")
    
    # LOGIC: If they type smash, we use the math function and end the program.
    if action == "smash":
        final_savings = count_money(coins_inside)
        print(f"CRASH! You saved RM {final_savings}! The program is over.")
        break
        
    elif action == "add":
        try:
            # ERROR CATCHING: Make sure they put in real number money.
            new_coin = float(input("How much is the coin worth? RM "))
            
            # MATH/LOGIC: You can't put negative money into a bank!
            if new_coin <= 0:
                print("You can't add zero or negative money!")
            else:
                coins_inside.append(new_coin)
                print("Clink! Coin added.")
                
        except ValueError:
            print("That's a button, not a coin! Type a number.")
    else:
        print("I don't understand that command. Type 'add' or 'smash'.")