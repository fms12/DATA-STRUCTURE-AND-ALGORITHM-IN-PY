def pattern(n):
    if(n==0):
        return
    for _ in range(n):
        print("*",end=' ')
    print("")
    pattern(n-1)


n = int(input())
pattern(n)

# skipcq
"""
* * * * * 
* * * * 
* * * 
* * 
*
"""
