#print program purpose
print("This program finds the value with the most duplicates in a list of numbers.")

#initialize number count
number_count = {}

#prompt user to enter number
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    try:
        number = int(user_input)
        number_count[number] = number_count.get(number, 0) + 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#find value with the most duplicates and print it
if number_count:
    most_duplicate_number = max(number_count, key=number_count.get)
    print(f"The number with the most duplicates is: {most_duplicate_number} (appeared {number_count[most_duplicate_number]} times)")
else:
    print("No valid numbers were entered.")

