def binary_search(array, search):
    # First index of array
    low = 0
    # Last index of array
    high = len(array) -1

    while low <= high:
        # The mid index of the array
        mid = (high + low) // 2
        # Check if search is in the right or left half of the array
        # If search is greater than the number in the middle of the array use the right half
        if array[mid] < search:
            low = mid + 1
        # If search is less than the number in the middle of the array use the left half
        elif array[mid] > search:
            high = mid - 1
        # If search is the number in the middle then return it
        else:
            return mid
    # If the number is not in the array return -1
    return -1

