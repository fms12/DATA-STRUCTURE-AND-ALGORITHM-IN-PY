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

![2](https://user-images.githubusercontent.com/68012074/104948553-7e849b00-59e3-11eb-9589-199dce7ca28c.png)

![3](https://user-images.githubusercontent.com/68012074/104948807-e33ff580-59e3-11eb-8c6a-e97a61ac5498.png)

![4](https://user-images.githubusercontent.com/68012074/104948809-e4712280-59e3-11eb-81c3-2d45c6396a0c.png)

![7886883b-6c77-4ad4-9289-670cb8a2d168_1610249138 248346](https://user-images.githubusercontent.com/68012074/104948846-f5ba2f00-59e3-11eb-855d-074ae2c32db5.png)

![f10111ae-7ff5-4036-8254-c13fe67f6cb4_1610249477 9338565](https://user-images.githubusercontent.com/68012074/104948855-f8b51f80-59e3-11eb-9f53-5322d5690c31.png)

![8](https://user-images.githubusercontent.com/68012074/104948903-0d91b300-59e4-11eb-9193-a9c1d2e7b6b1.png)

![10](https://user-images.githubusercontent.com/68012074/104948925-17b3b180-59e4-11eb-93bf-7705228c2443.png)













