# Program to Display Array Elements Using Recursion

def display_arr(a,i,n):
    if i>=n: # Base Case if value of i become greater or equal to size of an array then it returns
        return
    print(a[i],end=" ")
    display_arr(a,i+1,n)

arr = []
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array: ")
for i in range(0,n):
    num = int(input())
    arr.append(num)

print("Elements of Array are: ")
display_arr(arr,0,n)