# question:

# 1. You are given a number n, representing the size of array a.
# 2. You are given n numbers, representing elements of array a.
# 3. You are given a number k.
# 4. Rotate the array a, k times to the right
# (for positive values of k), and to
# the left for negative values of k.

# solution
def revrse(arr, k):
    # if the k is more than the lenght than modulw the array
    k = k % len(arr)
    # here if the array is negative than do the add with the length of array
    if (k < 0) :
        k += len(arr)

    # first part(array divded into 2 parts
    # first part start=0 and with len(arr)-k-1))
    rotate(arr, 0, len(arr)-k-1)
    rotate(arr, len(arr)-k, len(arr)-1)  # second part
    rotate(arr, 0, len(arr)-1)  # last part

    # join here to remove the braces form the array and comma form the array
    print(" ".join(map(str, arr)))


def rotate(arr, l, r):
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
k = int(input())
revrse(arr, k)


# //////////////////..............{output}.............////////////

# 3, 4, 5, 1, 2
