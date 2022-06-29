# First Index Of Occurrence
# you have given array size of n. so you have to return the first repeating number of index from given array 


# solution

def first(arr,i):
    if(i == len(arr)-1):
        return 
    
    if(arr[i]==arr[i+1]):
        return i
    return first(arr,i+1)
print(first([1,2,2,3,3,4,5],0))
