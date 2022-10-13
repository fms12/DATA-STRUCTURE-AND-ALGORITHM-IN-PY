# Python3 program to count the number
# of sub-matrices with all 1s

# Function to find required prefix-count
# for each row from right to left
def findPrefixCount(p_arr, arr):

    for i in range(0, n):
        for j in range(n - 1, -1, -1):

            if not arr[i][j]:
                continue

            if j != n - 1:
                p_arr[i][j] += p_arr[i][j + 1]

            p_arr[i][j] += arr[i][j]


# Function to count the number of
# sub-matrices with all 1s
def matrixAllOne(arr):

    # Array to store required prefix count of
    # 1s from right to left for boolean array
    p_arr = [[0 for i in range(n)] for j in range(n)]

    findPrefixCount(p_arr, arr)

    # variable to store the final answer
    ans = 0

    # Loop to evaluate each column of
    # the prefix matrix uniquely.
    # For each index of a column we will try to
    # determine the number of sub-matrices
    # starting from that index and has all 1s
    for j in range(0, n):

        i = n - 1

        # Stack to store elements and the count
        # of the numbers they popped

        # First part of pair will be the
        # value of inserted element.
        # Second part will be the count
        # of the number of elements pushed
        # before with a greater value */
        q = []

        # variable to store the number of
        # submatrices with all 1s
        to_sum = 0

        while i >= 0:

            c = 0
            while len(q) != 0 and q[-1][0] > p_arr[i][j]:

                to_sum -= (q[-1][1] + 1) * \
                            (q[-1][0] - p_arr[i][j])

                c += q[-1][1] + 1
                q.pop()

            to_sum += p_arr[i][j]
            ans += to_sum

            q.append((p_arr[i][j], c))
            i -= 1

    return ans


arr = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
n = 3
print(matrixAllOne(arr))
