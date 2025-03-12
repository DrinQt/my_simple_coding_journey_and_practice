#print the programs purpose
print("Input 10 numerical values, this program will print how many odd numbers are in there.")

#initialize the variable to store the number of odd numbers
odd_count = 0

#use a for loop to iterate through the range of numbers the user inputs and if the number is odd, add 1 to the variable storing the number of odd numbers
for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    if number % 2 != 0:
        odd_count += 1

#print the number of odd numbers the user inputted
print("The number of odd numbers is:", odd_count)


