def matrix(n):
    ob=[]
    for i in range(n):
        row=[]
        for  j in range(n):
            row.append(int(input()))
        ob.append(row)
    # transpose
    for i in range(len(ob)):
        for j in range(i,len(ob[0])):
            ob[i][j],ob[j][i]=ob[j][i],ob[i][j]
    # rotate the matrix
    for i in range(len(ob)):
        l=0
        r=len(ob[0])-1
        while(l<=r):
            ob[i][l],ob[i][r]=ob[i][r],ob[i][l]
            l+=1
            r-=1
    for i in  range(len(ob)):
        temp=[]
        for j in range(len(ob[0])):
            temp.append(ob[i][j])
        print(" ".join(map(str,temp)))
            
    
    
    
n=int(input())
matrix(n)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..input >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
4
11
12
13
14
21
22
23
24
31
32
33
34
41
42
43
44

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..output >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
41 31 21 11
42 32 22 12
43 33 23 13
44 34 24 14


















