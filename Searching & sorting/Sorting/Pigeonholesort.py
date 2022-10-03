# Algorithm
# At first, we will find the maximum as well as the minimum value in the array. Finding the max and the min value, we can easily calculate the range as (max-min +1)
# Now, we will create an empty array having the same size as the range. The space of the array is why this array is known as pigeonholes.
# Now, we will iterate through the original array and put each element in its respective pigeonhole. The pigeonhole of an element a[i] is calculated as the index a[i]-mini
# Lastly, in the initial array, we will reinsert the filled holes

def pigeonhole_sort(a):
    minimum = min(a)
    maximum = max(a)
    size = maximum - minimum + 1
    pigeonholes = [0] * size
    for i in a:
        pigeonholes[i - minimum] += 1
    j = 0
    for count in range(size):
        while pigeonholes[count] > 0:
            pigeonholes[count] -= 1
            a[j] = count + minimum
            j += 1
              
  
a = [12, 16, 19, 10,  9]
print("The array is :")
print(a)
print("Sorted array is :")
pigeonhole_sort(a)
print(a)


# Time complexity: O(n+K)
# Space complexity: O(n+K)
