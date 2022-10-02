#Program for finding the factorial of a number

def factorial(n):
    if n == 0:#base case
        return 1 #checks if n == 0 than it returns 1
    return n * factorial(n-1) #recursive call

n = int(input("Enter the number:"))#Taking input form user
print(factorial(n))#calling the function
