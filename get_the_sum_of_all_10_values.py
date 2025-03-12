#print the programs purpose
print("This program sums up all 10 numerical values.")

#initialize the sum variable to 0
total_sum = 0 

#use for loop to iterate 10 times and prompt the user to enter a number
for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    
#add the number to the sum
#print the sum of all 10 numbers