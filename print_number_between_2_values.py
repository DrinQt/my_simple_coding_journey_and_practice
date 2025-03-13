#print the program purpose
print("This program will print all numbers between the two values you input, excluding the values themselves.")

#use 'start' and 'end' to get the range of numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

#use if condition to check if the number is between the range and vice versa
#use for loop to print the numbers between the range
if start == end:
    print("There are no numbers between the two values since they are equal.")
else:
    lower = min(start, end)
    upper = max(start, end)
    for num in range(lower + 1, upper):
        print(num)