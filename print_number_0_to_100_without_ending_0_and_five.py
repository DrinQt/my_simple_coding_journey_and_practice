#print the purpose of the program
print("This program will print all numbers from 0 to 100 except numbers ending in zero or five.")

#set 'num' to 0
num = 0

#while 'num' is less than 100 use if statement to check if 'num' is not equal to 0 and 'num' is not divisible by 5
#print 'num'
#increment 'num' by 1
while num <= 100:
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1
    
