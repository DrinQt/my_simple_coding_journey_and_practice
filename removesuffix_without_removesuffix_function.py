#use custom function to remove suffix from string
def custom_removesuffix(s, suffix):
    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s

#Print the string without the suffix
print(custom_removesuffix("WassupBro", "Bro"))
