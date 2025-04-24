menus = {
    "Chicken": 4500.00,
    "Spaghetti": 7500.00,
    "Burger": 8000.00,
    "Fries": 4000.00
}

drinks = {
    "Coke": 45.00,
    "Royal": 45.00,
    "Sprite": 45.00,
    "MDew": 46.00
}

cart_food = []
cart_drink = []

print("\n------- FOOD MENU -------")
for key, value in menus.items():
    print(f'{key:10}: {value:.2f}')
print("------------------------------\n")

print("\n------- DRINKS MENU -------")
for key, value in drinks.items():
    print(f'{key:10}: {value:.2f}')
print("------------------------------\n")

while True:
    food = input("Pick an order: ").title()
    drink = input("Choose a drink: ").title()
    
    if food in menus and drink in drinks:
        cart_food.append(food)
        cart_drink.append(drink)
    else:
        print("Invalid food or drink choice!")
        continue  # skip the rest and retry
    
    order = input("Order again ( press 'enter' & 'e' exit ): ")
    if order.lower() == 'e':
        break


total_food = sum(menus[food] for food in cart_food)
total_drinks = sum(drinks[drink] for drink in cart_drink)
total = total_food + total_drinks

print("\nYour order:")
for i in range(len(cart_food)):
    print(f"{cart_food[i]} with {cart_drink[i]}")

print(f"\nTotal amount: ${total:,.2f}")
