#use custom index function
def custom_index(s, sub):
    sub_len = len(sub)
    for i in range(len(s) - sub_len + 1):
        if s[i:i + sub_len] == sub:
            return i
    raise ValueError(f"'{sub}' is not in string")

#print results
print(custom_index("Hello World", "World"))
