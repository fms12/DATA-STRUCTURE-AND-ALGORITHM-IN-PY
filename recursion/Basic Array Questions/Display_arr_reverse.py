# Program to print an array in reverse order

def reverse(a,n):
    if n==0:  # Base Case when size of array is 0 then it returns
        return
    else:
        print(a[n-1],end=" ")  # Print the last element of the array
        reverse(a,n-1)  # Function calling itself


a = [1, 42, 45, 60, 50, 10, 2]  # Taking an array
n = len(a)
reverse(a,n)

# Output
# 2 10 50 60 45 42 1
