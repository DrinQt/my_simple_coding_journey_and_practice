#print the purpose of the program
print("This program converts a name to pascal case")

#ask the user for a name
name = input("Enter a name: ")

#convert the name to pascal case
pascal_case = ''.join(word.capitalize() for word in name.split())

#print the name in pascal case
print(pascal_case)
