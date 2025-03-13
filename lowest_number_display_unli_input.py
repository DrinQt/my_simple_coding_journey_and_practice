#print the program purpose
print("This program will display the lowest number from the input numbers.")

#initialize lowest number to 0
lowest_number = None

#initialize the loop to True
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    try:
        number = float(user_input)
        #update the lowest number
        if lowest_number is None or number < lowest_number:
            lowest_number = number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#display the lowest number if valid
if lowest_number is not None:
    print("The lowest number entered is:", lowest_number)
else:
    print("No valid numbers were entered.")
