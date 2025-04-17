# Karen-Derya Ordering System

# Menu dictionaries
food_menu = {
    'Chicken': 45,
    'Adobo Baboy': 30,
    'Tinola': 25,
    'Pansit': 20
}

drink_menu = {
    'Coke': 20,
    'Mountain Dew': 25,
    'Sprite': 20,
    'Royal': 20,
    'Tea': 15,
    'Water': 12
}

order_items = []

# Function to display menus
def display_menu(menu_dict, menu_type):
    print(f"\n--- {menu_type} Menu ---")
    for item, price in menu_dict.items():
        print(f"{item} - ₱{price}")

# Start
print("---------------------")
print(" 1. Display Menu")
print(" 2. End Program")

option = int(input("\nEnter an option: "))
if option == 2:
    print("Exiting program. Goodbye!")
    exit()

# Ordering loop
while True:
    display_menu(food_menu, "Food")
    food_choice = input("\nSelect a food item (or type 'done' to finish): ").title()
    if food_choice.lower() == 'done':
        break
    if food_choice in food_menu:
        quantity = int(input(f"How many orders of {food_choice}?: "))
        order_items.append({
            'item': food_choice,
            'price': food_menu[food_choice],
            'quantity': quantity
        })
    else:
        print("Item not found in food menu.")

    display_menu(drink_menu, "Drink")
    drink_choice = input("\nSelect a drink (or type 'skip' to skip / 'cancel' to remove last item): ").title()

    if drink_choice.lower() == 'cancel' and order_items:
        removed_item = order_items.pop()
        print(f"Removed last item: {removed_item['item']}")
        continue
    elif drink_choice.lower() == 'skip':
        continue
    elif drink_choice in drink_menu:
        quantity = int(input(f"How many {drink_choice}?: "))
        order_items.append({
            'item': drink_choice,
            'price': drink_menu[drink_choice],
            'quantity': quantity
        })
    else:
        print("Item not found in drink menu.")

# Order Summary
print("\n====== Order Summary ======")
total = 0
for order in order_items:
    item_total = order['price'] * order['quantity']
    total += item_total
    print(f"{order['item']} x {order['quantity']} = ₱{item_total}")

print(f"\nTotal Bill: ₱{total}")
print("===========================")
