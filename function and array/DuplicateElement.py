#  find Duplicate in the array
# left most repeating element 
#  its can also work for the strings

for i in range(len(arr)):
    count[arr[i]]+=1
for j in range(len(arr)):
    if(count[arr[j]]>1):
        return arr[j]
return -1
# 2 approch
for i in range(len(arr)):
    if(count[arr[i]]==False):
        count[arr[i]] = True
    else:
        return arr[i]
return -1
