#def custom title function
def custom_title(s):
    return ' '.join(word.capitalize() for word in s.split())

#print result
print(custom_title("hello sir! im so handsome."))