#print program purpose
print("This program will determine if a number is unique or duplicate.")

#initialize set to keep track of entered numbers
entered_numbers = set()

#use exit condition to stop the loop
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break
#convert input to integer
#check if number is unique or duplicate
#print the result
