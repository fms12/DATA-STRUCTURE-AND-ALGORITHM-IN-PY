def binary_search(array, search):
    low = 0
    high = len(array) -1

    while low <= high:
        mid = (high + low) // 2

        if array[mid] < search:
            low = mid + 1
        elif array[mid] > search:
            high = mid - 1
        else:
            return mid
    return -1

