import os
import time


menus = {
    "Chicken": 45.00,
    "Fries": 25.00,
    "Spaghetti": 50.00,
    "Burger": 45.00
}

drinks = {
    "Coke": 15.00,
    "Royal": 15.00,
    "Sprite": 15.00,
    "Lemon Tea": 15.00,
}

food_cart = []
drink_cart = []
food_quantity = []
drink_quantity = []
total = 0

while True:
    print('-------- FOOD MENU --------')
    for key, value in menus.items():
        print(f'{key:10}: {value:15.2f}')
    print('---------------------------')

    print('-------- DRINK MENU --------')
    for key, value in drinks.items():
        print(f'{key:10}: {value:15.2f}')
    print('---------------------------')

    try:
        food = input('\nChoose food menu: ').title()
        food_qty = int(input(f'How many {food}s would you like to order? '))
        drink = input('\nChoose drink menu: ').title()
        drink_qty = int(input(f'How many {drink}s would you like to order? '))

        if food in menus and drink in drinks:
            food_cart.append(food)
            drink_cart.append(drink)
            food_quantity.append(food_qty)
            drink_quantity.append(drink_qty)
        else:
            print("Invalid menu or drink choice.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

    except ValueError:
        print("Please enter a valid number for quantity.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    option = input('Do you want to order again (y/n): ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if option.lower() == 'n':
        break

# Calculate total based on quantity
food_total = sum(menus[food] * food_quantity[i] for i, food in enumerate(food_cart))
drink_total = sum(drinks[drink] * drink_quantity[i] for i, drink in enumerate(drink_cart))
total = food_total + drink_total

print("YOUR ORDER: ")
for i in range(len(food_cart)):
    print(f"\n {food_cart[i]} = {food_quantity[i]}  with  {drink_cart[i]} = {drink_quantity[i]} ")

print(f'Total amount: ${total:,.2f}')
