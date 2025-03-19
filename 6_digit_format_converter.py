#print purpose of the program
print("This program converts a number to a 6 digit format")

#ask user  to input 0-1000
number = int(input("Please enter a number (0-1000): "))

#convert and print the number in 6 digit format
if 0 <= number <= 1000:
    print(f"{number:06}")
else:
    print("The number is not in the range 0-1000")

