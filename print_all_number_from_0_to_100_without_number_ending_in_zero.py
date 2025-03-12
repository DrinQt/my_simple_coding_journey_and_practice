#print the programs purpose
print("This program will print all numbers between 0 and 100 except numbers ending in zero.")

#use a for loop to iterate through the numbers 0 to 100
#use an if statement to check if the number ends in 0. Use if not to check if the number does not end in 0.
#use the print() function to print the number
for number in range(101):
    if number % 10 != 0:
        print(number)