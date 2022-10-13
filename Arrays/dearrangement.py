# Python program for the above approach

# Declaring a dp array
dp = [-1]*(1 << 20)


# Function to return
# the factorial of a number
def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


# Function to count the
# Number of derangements
def countDerangements(i, mask, n, A):

    # If all the numbers are placed,
    # then return 1.
    if (mask == (1 << n) - 1):
        return 1

    # If the state has already been computed,
    # then return it
    if (dp[mask] != -1):
        return dp[mask]

    dp[mask] = 0

    # Check for all possible numbers
    # that can be placed in
    # the current position 'i'.
    for j in range(n):

        # If the current element arr[j]
        # Is not yet selected
        # (bit 'j' is unset in mask),
        # And if arr[i]!= arr[j]
        # (to ensure derangement).
        if (mask & (1 << j) == 0 and (A[i] != A[j])):

            # Set the bit 'j' in mask and
            # Call the function
            # For index 'i + 1'.
            dp[mask] += countDerangements(i + 1, mask | (1 << j), n, A)

    # Return dp[mask]
    return dp[mask]


# Utility Function to count
# The number of derangements
def UtilCountDerangements(A, N):
    frequencyMap = {}
    for i in range(N):
        if A[i] in frequencyMap:
            frequencyMap[A[i]] = frequencyMap[A[i]]+1
        else:
            frequencyMap[A[i]] = 1

        # Function call and storing
        # The return value in 'ans'.
    ans = countDerangements(0, 0, N, A)

    # Iterating through the HashMap
    for value in frequencyMap.items():

        # Frequency of current number
        times = value

        # If it occurs more than 1 time,
        # divide the answer by its frequency.
        if (times > 1):
            ans = ans // factorial(times)
    return ans


# Driver code
# Input array
arr = [ 1, 2, 2, 3, 3 ]

# Size of array
N = len(arr)
print(UtilCountDerangements(arr, N))
