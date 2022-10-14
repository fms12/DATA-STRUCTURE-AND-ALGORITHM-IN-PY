# Program for finding the number of  zeros in a given number
def countZeros(n):
    if n == 0:  # base case
        return 0  # return 0 if n == 0
    smallOutput = countZeros(n // 10)  # recursion call
    # adding and smallOutput vaule + 1 and divide using 2^n
    if n % 10 == 0:
        return smallOutput + 1
    else:
        return smallOutput


n = int(input("Enter the number: "))  # taking input from user
print(countZeros(n))  # calling the function and printing the result
