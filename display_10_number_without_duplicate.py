#print the program purpose
print("This program will display 10 numbers without duplicate")

#initialize the number list
number_list = []

#prompt the user to enter 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    number_list.append(num)


#find the unique numbers from the list
unique_numbers = [num for num in number_list if number_list.count(num) == 1]

#display the unique numbers
print("Numbers without duplicates:", unique_numbers)


