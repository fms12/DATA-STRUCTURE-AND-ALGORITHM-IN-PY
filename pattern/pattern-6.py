# Left Triangle number Pattern

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n = int(input("Enter value: "))
#  Two nested loops where the inner loop will print the number of times the 
# outer loop is executed and print the number in every iteration.
for i in range(n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()