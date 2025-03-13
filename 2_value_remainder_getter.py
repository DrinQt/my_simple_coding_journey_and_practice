#print the purpose of the program
print("This program gets the remainder of the first number when divided by the second number.")

#prompt the user to enter a number
num1 = int(input("Enter the first number: "))

#prompt the user to enter a divisor
num2 = int(input("Enter the second number: "))

#calculate the remainder of the division using the modulus operator
remainder = num1 % num2

#print the remainder
print("The remainder of the first number when divided by the second number is:", remainder)