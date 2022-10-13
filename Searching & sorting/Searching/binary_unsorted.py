def binarySearch(array, target, left, right):
    print("*************")
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]
    print(array)
    print("middle element:" + str(potentialMatch))
    print("extreme left:" + str(leftNum))
    print("extreme right:" + str(rightNum))

    if target == potentialMatch:
        print("target == potentialMatch")
        return middle

    elif leftNum <=potentialMatch:
        print("leftNum <=potentialMatch")
        if leftNum <= target < potentialMatch:
            print("target < potentialMatch and target >=leftNum")
            return binarySearch(array, target, left , middle - 1)
        else:
            print(" target > potentialMatch and target <=leftNum")
            return binarySearch(array, target, middle+1, right)
    else:
        print("leftNum >=potentialMatch")
        if potentialMatch < target <=rightNum:
            print("target > potentialMatch and target <=rightNum")
            return binarySearch(array, target, middle+1, right)
        else:
            print("target < potentialMatch and target >=rightNum")
            return binarySearch(array, target, left, middle -1)


array = [45, 61, 71, 73, 76, 1, 2, 3, 33, 37]

target = 2
binarySearch(array, target, 0, len(array)-1)
