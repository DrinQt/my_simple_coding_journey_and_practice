#use custom capitalize function
def custom_capitalize(s):
    return s[0].upper() + s[1:].lower() if s else s

#print result
print(custom_capitalize("hello sir!"))
