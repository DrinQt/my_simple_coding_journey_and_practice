#print the purpose of the program
print("This program converts a name to snake case")

#prompt the user to enter a name
name = input("Enter a name: ")

#convert the name to snake case
snake_case = '_'.join(word.lower() for word in name.split())

#display the name in snake case
print(snake_case)

