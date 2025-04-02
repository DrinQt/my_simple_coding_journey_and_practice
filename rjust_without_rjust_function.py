#use custom function to right justify a string
def custom_rjust(s, width):
    return ' ' * (width - len(s)) + s if width > len(s) else s


#print right justified string
