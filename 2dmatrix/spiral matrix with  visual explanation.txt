def matrix(n,m):
    ob=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(int(input()))
            
        ob.append(row)
    res = []
    row_begin = 0
    col_begin = 0
    row_end = len(ob)-1 
    col_end = len(ob[0])-1
    while (row_begin <= row_end and col_begin <= col_end):
            for i in range(row_begin,row_end+1):
                res.append(ob[i][col_begin])
            col_begin += 1
            for i in range(col_begin,col_end+1):
                res.append(ob[row_end][i])
            row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(ob[i][col_end])
                col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(ob[row_begin][i])
                row_begin += 1
    print("\n".join(map(str,res)))
        
n=int(input())
m=int(input())
matrix(n,m)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


![1](https://user-images.githubusercontent.com/68012074/104948158-de2e7680-59e2-11eb-9741-27a7957696b4.png)











