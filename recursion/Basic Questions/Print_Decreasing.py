# Program for print the decreaseing number
def printDecreasing(n):
    if n == 0:  # base case
        return
    print(n)  # printing  the number one by one
    printDecreasing(n-1)  # recursive call


n = int(input("Enter the number:"))  # Taking input form user
printDecreasing(n)  # calling the function
