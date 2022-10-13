# Program for finding the power of a number using log
def power_logarithmic(x, n):

    if n == 0:  # base case
        return 1  # checks if n == 0 than it returns 1

    # n//2 rounds the number to the nearest integer
    power = power_logarithmic(x, n//2)  # recursive call

    if n % 2 == 0:  # checks if n is even
        return power * power  # if n is even than it returns power * power

    else:
        return x * power * power  # if n is odd than it returns x * power * power


x = int(input("Enter the  number:"))  # Taking input of a number form user
n = int(input("Enter the power:"))  # Taking input of power from user
print(power_logarithmic(x, n))  # calling the function
