# Program to find first index of occurrence of an element in an array

def firstindex(a, x, si):
    l = len(a)
    if si==l: # Base Case if size of array is 1 then it returns -1
        return -1
    if a[si]==x:
        return si
    return firstindex(a,x,si+1)

a = [1,4,3,7,5,4,6]
x = 4
print(firstindex(a, x,0))