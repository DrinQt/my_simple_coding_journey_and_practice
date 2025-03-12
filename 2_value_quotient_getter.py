#print the programs purpose
print("This program gets the quotient of two numerical values.")

#prompt the user to enter a numerator
num1 = float(input("Enter the numerator: "))

#prompt the user to enter a denominator
num2 = float(input("Enter the denominator: "))

#calculate the quotient of the numerator and denominator use if statement to check if the denominator is zero
if num2 != 0:
    quotient = num1 / num2
#display the quotient of the numerator and denominator
    print("The quotient of the two numbers is:", quotient)
else:
    print("Error: Division by zero is not allowed.")