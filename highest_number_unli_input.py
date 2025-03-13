# Print the program purpose
print("This program will display the highest number you entered.")

# Set variable to store the highest number
highest_number = None

# Prompt the user to enter a number
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    try:
        number = float(user_input)  # Convert input to a float

        # Update the highest number
        if highest_number is None or number > highest_number:
            highest_number = number

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Display the highest number if valid
if highest_number is not None:
    print("The highest number entered is:", highest_number)
else:
    print("No valid numbers were entered.")