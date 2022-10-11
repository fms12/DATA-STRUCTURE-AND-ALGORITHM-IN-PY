def pigeonhole_sort(a):
    # size of range of values in the list (ie, number of pigeonholes we need)
    min_val = min(a)  # min() finds the minimum value
    max_val = max(a)  # max() finds the maximum value
    size = max_val - min_val + 1  # size is difference of max and min values plus one
    # list of pigeonholes of size equal to the variable size
    holes = [0] * size
    # Populate the pigeonholes.
    for x in a:
        assert isinstance(x, int), "integers only please"
        holes[x - min_val] += 1
    # Putting the elements back into the array in an order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + min_val
            i += 1
            
nums = [4, 3, 5, 1, 2]
print("\nOriginal list:")
print(nums)
pigeonhole_sort(nums)
print("Sorted order is:", nums)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(nums)
pigeonhole_sort(nums)
print("Sorted order is:", nums)
