#def custom swapcase(s):
def custom_swapcase(s):
    return ''.join(char.swapcase() for char in s)

#print result
print(custom_swapcase("Hello Sir!"))