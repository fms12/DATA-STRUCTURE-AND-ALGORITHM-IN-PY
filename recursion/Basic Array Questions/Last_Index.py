# Program to find last index of occurrence of an element in an array

def lastindex(a, x, si):
    l = len(a)
    if si==l: # Base Case if size of array is 1 then it returns -1
        return -1
    smallerListOutput = lastindex(a, x, si+1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if a[si]==x:
            return si
        else:
            return -1

a = [1,2,4,6,7,8,4,7,6]
x = 4
print(lastindex(a,x,0))