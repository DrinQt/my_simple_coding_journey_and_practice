#define custom center function
def custom_center(s, width):
    total_spaces = width - len(s)
    return ' ' * (total_spaces // 2) + s + ' ' * (total_spaces - total_spaces // 2)

#print center function
print(custom_center("Hello", 11))
