# Program to find first index of occurrence of an element in an array
# Using start index approach, in this we don't have to make the copy of an array


def firstindex(a, x, si):
    l = len(a)
    if si==l: # Base Case if size of array is 1 then it returns -1
        return -1
    if a[si]==x: # If element at the index si is equal to the value of x 
        return si # Then it will return index si
    return firstindex(a,x,si+1) # Function calling itself with the increment of si

a = [1,4,3,7,5,4,6] # Taking an Example
x = 4 # Find the first index of 4
print(firstindex(a, x,0))

# Ouput: 
# 1
