def sumarray(arr1,arr2):
    i=len(arr1)-1   
    j=len(arr2)-1
    s=[]
    c=0
    while(i>=0 or j>=0):
        d=c
        if (i >= 0): 
            d += arr1[i]
        if (j >= 0):
            d += arr2[j]
        c = d // 10 
        d = d % 10
        s.append(d)
        i-=1
        j-=1
    if (c > 0):
        s.append(c)    
    s.reverse()
    print("".join(map(str,s)))
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
sumarray(arr1,arr2)

...........//////////////////////.........output..........//////////////////////...........................


9 9 9

2 8

solution = 1027



# ///////////////////////////you can right like this also/////////////////////////
def sumarray(arr1,arr2):
    i=len(arr1)-1   
    j=len(arr2)-1
    s=[]
    c=0
    while(i>=0 or j>=0):
        d=c
        if (i >= 0): 
            d += arr1[i]
        if (j >= 0):
            d += arr2[j]
        c = d // 10 
        d = d % 10
        s.append(d)
        i-=1
        j-=1
    if (c > 0):
        s.append(c)    
    s.reverse()
# given output in diffrent line
    for i in range(len(s)):
        print(s[i])
        
# taking input in diffrent line  so it can easy for the pep solution
arr1=[]
n1=int(input())
for i in range(n1):
    arr1.append(int(input()))
    
arr2=[]
n2=int(input())
for i in range(n2):
    arr2.append(int(input()))
    
sumarray(arr1,arr2)
