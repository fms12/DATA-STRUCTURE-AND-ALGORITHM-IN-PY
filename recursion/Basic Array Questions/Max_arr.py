# Program to find maximum element in an array using recursion

def max_arr_rec(a,n):
    if n==1: # Base Case if array containing only one element then return it
        return a[0]
    else:
        previous = max_arr_rec(a,n-1) # calling function itself and storing in variable called prevoius
        current = a[n-1] # that means previous element from the sequence and check the value with the next element in the sequence which is current
        if previous > current: # comparing both and returing the max of these values
            return previous
        else: 
            return current

a = [1, 42, 45, 60, 50, 10, 2] # Taking an array for example
n = len(a) # length of the array
print(max_arr_rec(a,n))

# Output:
# 60
