# Define a dictionary to map month numbers to month names
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

try:
    # Get user input for the month number
    month_number = int(input("Enter the month number (1-12): "))

    # Check if the input is valid
    if 1 <= month_number <= 12:
        # Print the corresponding month name
        print(f"Month name for {month_number} is: {month_names[month_number]}")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
