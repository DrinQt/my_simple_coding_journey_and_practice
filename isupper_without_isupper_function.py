#define isupper_without_isupper_function.py
def custom_isupper(s):
    return all(char.isupper() for char in s)

#print result of isupper function without using isupper function