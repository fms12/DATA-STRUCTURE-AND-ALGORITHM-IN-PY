# Program to Display Array Elements Using Recursion

def display_arr(a,i,n):

    # Base Case if value of i become greater
    # or equal to size of an array then it returns
    if i>=n:
        return

    # Print the array at ith position
    # (as the value of i increases elements get print accordingly)
    print(a[i],end=" ")
    display_arr(a,i+1,n)  # Function calling itself


arr = []  # Taking an Array

# Initializing the size of an array
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array: ")
for i in range(0,n):
    num = int(input())  # Taking input from user
    arr.append(num)

print("Elements of Array are: ")
display_arr(arr,0,n)  # Printing the elements of an array through recursion

# Example
# Input:
# 1
# 2
# 3
# 4
# 5

# Ouput:
# 1 2 3 4 5
