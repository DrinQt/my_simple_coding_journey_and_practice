#print the programs purpose
print("This program calculates the result of the first value raised to the power of the second value")

#get the first value from the user
num1 = float(input("Enter the base number (first number): "))

# get the second value from the user
num2 = float(input("Enter the exponent number (second number): "))

# calculate the result of the first value raised to the power of the second value
result = num1 ** num2

# print the result
print(f"{num1} raised to the power of {num2} is: {result}")