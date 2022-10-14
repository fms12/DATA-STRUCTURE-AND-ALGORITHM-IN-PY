# Program to find maximum element in an array using recursion

def max_arr_rec(a,n):
    # Base Case if array containing only one element then return it
    if n==1:
        return a[0]
    else:
        # calling function itself and storing in variable called prevoius
        previous = max_arr_rec(a,n-1)

        # that means previous element from the sequence and check the value
        # with the next element in the sequence which is current
        current = a[n-1] 

        # comparing both and returing the max of these values
        if previous > current:
            return previous
        else: 
            return current


# Taking an array for example
a = [1, 42, 45, 60, 50, 10, 2]
n = len(a)  # length of the array
print(max_arr_rec(a,n))

# Output:
# 60
