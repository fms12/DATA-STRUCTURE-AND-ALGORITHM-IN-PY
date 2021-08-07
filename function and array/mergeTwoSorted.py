arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = [None]*(len(arr1) + len(arr2))
i =0
j= 0
k = 0
while(i<len(arr1) and j<len(arr2)):
    # for the arr check 
    if(arr1[i]<arr2[j]):
        arr3[k] = arr1[i]
        k+=1
        i+=1
    else:
        arr3[k]=arr2[j]
        k+=1
        j+=1
while(i<len(arr1)):
        arr3[k]=arr1[i]
        k+=1
        i+=1
while(j<len(arr2)):
        arr3[k]=arr2[j]
        k+=1
        j+=1
print(arr3)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# INPUT
# 1 3 5 7
# 2 4 6 8
OUTPUT:
  [1, 2, 3, 4, 5, 6, 7, 8]
