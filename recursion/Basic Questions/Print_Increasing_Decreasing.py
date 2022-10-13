# Program for printing the increasing and decreasing number in single function
def printIncreasingDecreasing(n):
    if n == 0:  # base case
        return
    print(n)  # printing the decreasing number one by one
    printIncreasingDecreasing(n-1)  # recursive call
    print(n)  # printing the increasing number one by one


n = int(input("Enter the number:"))  # Taking input form user
printIncreasingDecreasing(n)  # calling the function
