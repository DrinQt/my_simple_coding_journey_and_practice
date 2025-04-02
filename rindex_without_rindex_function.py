#use custom_rindex function to find the last occurrence of a substring in a string
def custom_rindex(s, sub):
    sub_len = len(sub)
    for i in range(len(s) - sub_len, -1, -1):
        if s[i:i + sub_len] == sub:
            return i
    raise ValueError(f"'{sub}' is not in string")

#print result
print(custom_rindex("WassupBro", "Bro"))

