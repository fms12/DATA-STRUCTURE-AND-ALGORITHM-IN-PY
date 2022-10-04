#  find Duplicate in the array
def solution(arr):
    count=[]
    for i,element in enumerate(arr):
        if arr[i] in count:
            return arr[i]
        else:
            count.append(arr[i])
    return -1
print(solution([1,2,3,4,5]))
