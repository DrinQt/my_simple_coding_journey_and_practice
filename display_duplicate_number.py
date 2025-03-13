#print program purpose
print("This program will display duplicate numbers in a list of 10 numbers")

#initialize a list to store the numbers
numbers = []

#prompt the user to enter 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

#find the duplicate numbers and display them
duplicates = set(num for num in numbers if numbers.count(num) > 1)

print("Numbers with duplicates:", duplicates) if duplicates else print("No duplicates found.")
