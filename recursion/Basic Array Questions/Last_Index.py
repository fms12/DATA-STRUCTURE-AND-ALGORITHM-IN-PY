# Program to find last index of occurrence of an element in an array
# We will use start index approach

def lastindex(a, x, si):
    l = len(a)
    if si==l: # Base Case if size of array is 1 then it returns -1
        return -1
        
    smallerListOutput = lastindex(a, x, si+1) # calling function itself
    
    if smallerListOutput != -1: # if smallerListOuput returns -1 then it will return smallerListOuput itself
        return smallerListOutput # means when in smallerListOuput, value of si becomes equal to length of array
        # it means no element found then it will return -1
    else:
        if a[si]==x: # if element at si is equal to x then it will return index si
            return si
        else:
            return -1 # else return -1

a = [1,2,4,6,7,8,4,7,6] # Taking an array for example
x = 4 # Find the last index of occurrence of 4
print(lastindex(a,x,0))

# Output:
# 6
