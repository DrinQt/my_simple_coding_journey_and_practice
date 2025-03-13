#print the purpose of the program
print("This program prints the result when you subtract each of the next nine values from the first value.")

#prompt the user to enter the first number and use range function to get the remaining numbers
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

#set the first number to a variable 0
first_number = numbers[0]

#use a for loop to iterate through the remaining numbers and subtract the first number from the remaining numbers
for num in numbers[1:]:
    print(first_number - num)