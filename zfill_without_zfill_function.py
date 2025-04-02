#use custom function to pad a string with leading zeros
def custom_zfill(s, width):
    return '0' * (width - len(s)) + s if width > len(s) else s

#print the result
