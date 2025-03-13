#print purpose of the program
print("This program calculates the average of numbers entered by the user.")

#Set the variable 'total' to 0 and 'count' to 0
total = 0
count = 0

#prompt the user to enter a number
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    try:
        total += float(user_input)  # Add the number to the total
        count += 1                   # Increment the count
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#calculate and display avegare of the numbers entered
if count > 0:
    print("The average is:", total / count)
else:
    print("No valid numbers were entered.")