#print the purpose of the program
print("This program will print the lowest and highest number you enter.")   

#initialize a list to store the numbers
numbers = []

#use while true loop to get the input from the user
while True:
    number = input("Enter a number or type 'done' to see the result: ")
    #check if the user entered 'done'
    if number == 'done':
        break
    #add the number to the list
    numbers.append(int(number))

#sort the list in ascending order
#print the number from lowest to highest
