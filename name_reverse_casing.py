#print the purpose of the program
print("This program will reverse the casing of your name.") 

#ask the user to enter their name
name = input("Enter your name: ")

#reverse the casing of the name
reversed_casing = ''.join(char.swapcase() for char in name)

#print the reversed casing of the name
print(reversed_casing)

