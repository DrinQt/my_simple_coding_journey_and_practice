#print program purpose
print("This program will determine if a number is unique or duplicate.")

#initialize set to keep track of entered numbers
entered_numbers = set()

#use exit condition to stop the loop
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break
try:
        # Convert input to an integer
        number = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if number in entered_numbers: #check if number is unique or duplicate
        print("Duplicate")
    else:
        print("Unique")
        entered_numbers.add(number)
