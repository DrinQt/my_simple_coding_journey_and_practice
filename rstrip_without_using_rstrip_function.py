#use custom rstrip function to remove trailing characters from a string
def custom_rstrip(s):
    while s and s[-1] == ' ':
        s = s[:-1]
    return s

#print result
print(custom_rstrip("Wassup Bro!    "))

