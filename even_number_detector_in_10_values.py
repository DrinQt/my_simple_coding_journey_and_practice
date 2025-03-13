#print the program purpose
print("This program counts how many even numbers you will input.")

#set even number counter to 0
even_count = 0

#use for loop to iterate 10 times and 'if' statement to check if the number is even.
#If the number is even, increment the even number counter by 1
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_count += 1

#print the even number counter
print("There are", even_count, "even numbers.")