# Python program to display the Fibonacci sequence
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)  # recursion call


count = int(input("Enter the limit: "))

# check if the number of terms is valid
if count<=0:
    print("Enter a number greater than 0")
else:
    for i in range(count):
        print(fib(i),end=" ")
