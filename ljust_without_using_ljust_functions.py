#def custom ljust(string, width):
def custom_ljust(s, width):
    return s + ' ' * (width - len(s))

#print result
print(custom_ljust("Hello", 10)) 
