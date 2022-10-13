n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print('*', end='	')
    print()


"""
OUTPUT
*
*	*
*	*	*
*	*	*	*
*	*	*	*	*
"""


# using recusrion
def printPatternRowRecur(n):
    # base condition
    if (n < 1):
        return

    # print the remnaining
    # stars of the n-th row
    # recursively
    print("*", end=" ")
    printPatternRowRecur(n - 1)


n = int(input())
printPatternRowRecur(n)
