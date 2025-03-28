#define custom removeprefix function
def custom_removeprefix(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

#print result of removeprefix function