def linearSearch(array, search):
    # Check every index of the array
    for i in range(len(array)):
        # If search is in the i index return it
        if array[i] == search:
                return i
    # If search is not in the array return -1
    return -1
