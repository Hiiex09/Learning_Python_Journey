# Shopping cart program

import os
import time

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    if not food.isalpha():
        print('You must enter a string')
    else:
        try:
            price = float(input(f'Enter the {food} price: '))
            foods.append(food)
            prices.append(price)
        except ValueError:
              print("Invalid input. Please enter a number.")
              time.sleep(2)
              os.system('cls' if os.name == 'nt' else 'clear')


print('----- YOUR CART -----')
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f'\nTotal amount: ${total:,.2f}')