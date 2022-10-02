# Program to print an array in reverse order

def reverse(a,n):
    if n==0: # Base Case when size of array is 0 then it returns
        return
    else:
        print(a[n-1])
        reverse(a,n-1)

a = [1, 42, 45, 60, 50, 10, 2]
n = len(a)
reverse(a,n)