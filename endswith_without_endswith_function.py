#define custom endswith function
def custom_endswith(s, suffix):
    return s[-len(suffix):] == suffix
 
 #print results
print(custom_endswith("hello sir", "sir")) #
