# use custom function to check if a string starts with a given prefix
def custom_startswith(s, prefix):
    return s[:len(prefix)] == prefix

#print result
print(custom_startswith("hello world", "hello"))  # True
print(custom_startswith("hello world", "world"))  # False