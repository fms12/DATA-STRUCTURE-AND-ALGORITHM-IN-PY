
def printIncreasingDecreasing(n):
    if n == 0:
        return
    print(n)
    printIncreasingDecreasing(n-1)
    print(n)

n = int(input("Enter the number:"))
printIncreasingDecreasing(n)
