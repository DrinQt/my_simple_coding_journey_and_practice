#print the purpose of the program
print("This program will sort numbers in descending order")

#set number variable to empty list
numbers = []

#prompt user to enter a number
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#sort and print the number in descending order
numbers.sort(reverse=True)
print("Numbers from highest to lowest:", numbers)

