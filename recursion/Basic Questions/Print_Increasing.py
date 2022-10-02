#Program for printing the increasing number
def printIncreasing(n):
    if n == 0: #base case
        return
    printIncreasing(n-1) #recursive call
    print(n) #printing the increasing number one by one

n = int(input("Enter the number:")) #Taking input form user
printIncreasing(n) #calling the function