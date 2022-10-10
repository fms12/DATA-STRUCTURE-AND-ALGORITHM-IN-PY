def bar(arr):
    height = max(arr)
    for i in range(height):
        for j in range(len(arr)):
            if(arr[j]>=height-i):
                print("*",end='\t')
            else:
                print(end='\t')
        print()
        
       
n=input()
arr=[int(i) for i in input().split()]
print(bar(arr))
