# A Python3 program to print union and intersection
# of two unsorted arrays

# Prints union of arr1[0..m-1] and arr2[0..n-1]


def printUnion(arr1, arr2, m, n):

    # Before finding union, make sure arr1[0..m-1]
    # is smaller
    if (m > n):
        (arr1, arr2) = (arr2, arr1)

        (m, n) = (n, m)

    # Now arr1[] is smaller

    # Sort the first array and print its elements (these two
    # steps can be swapped as order in output is not important)
    arr1.sort()
    for i in range(0, m):
        print(arr1[i], end=" ")

    # Search every element of bigger array in smaller array
    # and print the element if not found
    for i in range(0, n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1):
            print(arr2[i], end=" ")

# Prints intersection of arr1[0..m-1] and arr2[0..n-1]


def printIntersection(arr1, arr2, m, n):

    # Before finding intersection, make sure arr1[0..m-1]
    # is smaller
    if (m > n):
        (arr1, arr2) = (arr2, arr1)

        (m, n) = (n, m)

    # Now arr1[] is smaller

    # Sort smaller array arr1[0..m-1]
    arr1.sort()

    # Search every element of bigger array in smaller
    # array and print the element if found
    for i in range(0, n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) != -1):
            print(arr2[i], end=" ")

# A recursive binary search function. It returns
# location of x in given array arr[l..r] is present,
# otherwise -1


def binarySearch(arr, l, r, x):

    if (r >= l):
        mid = int(l + (r - l)/2)

        # If the element is present at the middle itself
        if (arr[mid] == x):
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        if (arr[mid] > x):
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        return binarySearch(arr, mid + 1, r, x)

    # We reach here when element is not present in array
    return -1


# Driver code
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
m = len(arr1)
n = len(arr2)

# Function call
print("Union of two arrays is ")
printUnion(arr1, arr2, m, n)
print("\nIntersection of two arrays is ")
printIntersection(arr1, arr2, m, n)
