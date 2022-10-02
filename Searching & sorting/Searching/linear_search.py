# Linear Search is a searching algorithm with complexity n
def linear_search(arr,key):
    # Transversing the array
    for index,elem in enumerate(arr):
        if elem==key: #Comparing the elements with key
            return index #returning the index of the matched position
    return -1 # if element is not found then -1 is returned


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = linear_search(arr, x)

if result != -1: #if element is found
    print("Element is present at index", str(result))
else: # if element is not found
    print("Element is not present in array")
