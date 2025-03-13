#print the purpose of the program
print("This program will display 10 numbers, showing duplicates only once.")

#initialize the list of numbers and seen set
number_list = []
seen_numbers = set()

#prompt the user to enter 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    number_list.append(num)

#display the 10 numbers, showing only the duplicates once
for number in number_list: 
    if number not in seen_numbers:
        print(number)
        seen_numbers.add(number)


