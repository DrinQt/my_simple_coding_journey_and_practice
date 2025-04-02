#use custom function to check if a string is lowercase
def custom_islower(s):
    for char in s:
        if 'A' <= char <= 'Z':
            return False
    return len(s) > 0

#print result
print(custom_islower("hello"))  # True
print(custom_islower("Hello"))  # False