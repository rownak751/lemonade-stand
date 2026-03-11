# PROGRAM 5: THE PIZZA BUILDER

# DATA STRUCTURE: A menu of toppings and how much they cost.
topping_prices = {"cheese": 1.0, "pepperoni": 2.0, "mushrooms": 1.5}
# An empty list for the pizza we are building.
my_pizza = []

# FUNCTION: A chef robot that calculates the bill.
def calculate_bill(pizza_list, prices_dict):
    total = 5.0 # Every pizza starts at $5 for the plain crust.
    # FOR LOOP: The chef looks at every topping on the pizza and adds the price.
    for top in pizza_list:
        total = total + prices_dict[top]
    return total

print("Let's build a pizza! Base pizza is RM 5.00.")

# WHILE LOOP: Keep adding toppings until the pizza is ready to bake.
while True:
    print("\nAvailable Toppings:")
    for t in topping_prices:
        print(f"- {t} (RM {topping_prices[t]})")
        
    choice = input("\nWhat topping do you want? (or 'bake' to cook it): ")
    
    # LOGIC: Stop the loop and cook if they say bake.
    if choice == "bake":
        break
        
    if choice in topping_prices:
        try:
            # ERROR CATCHING: How many scoops of this topping?
            scoops = int(input(f"How many scoops of {choice}? "))
            
            # MATH: A tiny loop that runs based on how many scoops they asked for.
            for i in range(scoops):
                my_pizza.append(choice)
            print(f"Added {scoops} scoops of {choice}!")
            
        except ValueError:
            print("You have to give me a whole number for scoops!")
    else:
        print("We don't have that topping.")

# We hand the pizza list to the chef function to get the final price.
final_price = calculate_bill(my_pizza, topping_prices)
print(f"\nYour pizza is out of the oven! Total cost is RM {final_price}")