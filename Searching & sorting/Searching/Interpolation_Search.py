# Function to determine if target exists in the sorted list `A` or not
# using an interpolation search algorithm
def interpolationSearch(A, target):

    # base case
    if not A:
        return -1

    # search space is A[left…right]
    (left, right) = (0, len(A) - 1)

    while A[right] != A[left] and A[left] <= target <= A[right]:

        # estimate mid
        mid = left + (target - A[left]) * (right - left) // (A[right] - A[left])

        # key is found
        if target == A[mid]:
            return mid
        # discard all elements in the right search space, including the middle element
        elif target < A[mid]:
            right = mid - 1
        # discard all elements in the left search space, including the middle element
        else:
            left = mid + 1

    # if the key is found
    if target == A[left]:
        return left

    # target doesn't exist in the list
    return -1


if __name__ == '__main__':

    A = [2, 5, 6, 8, 9, 10]
    key = 5

    index = interpolationSearch(A, key)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
