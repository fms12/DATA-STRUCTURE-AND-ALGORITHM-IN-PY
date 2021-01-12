def twoarray(n,m):
    for i in range(n):
        row=[] #here it will change line  it will print like 
        
        # 11 12 13 14
        #21 22 23 24
        
        for j in range(m):
            row.append(int(input()))
        print(" ".join(map(str,row)))
    

n=int(input())
m=int(input())
twoarray(n,m)
