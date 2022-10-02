# Program to find maximum element in an array using recursion

def max_arr_rec(a,n):
    if n==1: # Base Case if array containing only one element then return it
        return a[0]
    else:
        previous = max_arr_rec(a,n-1)
        current = a[n-1]
        if previous > current:
            return previous
        else: 
            return current

a = [1, 42, 45, 60, 50, 10, 2]
n = len(a)
print(max_arr_rec(a,n))