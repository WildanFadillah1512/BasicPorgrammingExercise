# Initialize the total cost
total_cost = 0

# Initialize the items dictionary to store item names and their prices
items = {
    1: {"name": "Lipstic", "price": 25},
    2: {"name": "Mascara", "price": 40},
    3: {"name": "Lotion", "price": 60}
}

while True:
    try:
        # Display the available items
        print("Available items:")
        for item_num, item_info in items.items():
            print(f"{item_num}. {item_info['name']} ${item_info['price']}")

        # Get user input
        user = int(input("Input your item number (0 to finish): "))
        if user == 0:
            break

        user_2 = int(input("The quantity: "))

        # Calculate the cost of the selected item
        if user in items:
            item_price = items[user]["price"]
            item_cost = user_2 * item_price
            print(f"Price Total {items[user]['name']} is: ${item_cost}\n")
            total_cost += item_cost
        else:
            print("Invalid number")

    except ValueError:
        print("Invalid input, please enter a number.")

# Calculate the discount
discount = 0
if total_cost >= 100:
    discount = 0.10
elif total_cost >= 50:
    discount = 0.05

# Calculate the final cost after applying the discount
final_cost = total_cost * (1 - discount)

# Display the total cost and any applicable discount
print(f"Total cost: ${total_cost:.2f}")
if discount > 0:
    print(f"Discount applied: {discount * 100:.0f}%")
    print(f"Final cost after discount: ${final_cost:.2f}")
else:
    print("No discount applied.")
