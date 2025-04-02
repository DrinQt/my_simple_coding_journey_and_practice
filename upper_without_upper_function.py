#use custom function to convert string to upper case
def custom_upper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

#print result
print(custom_upper("Okay na to."))
