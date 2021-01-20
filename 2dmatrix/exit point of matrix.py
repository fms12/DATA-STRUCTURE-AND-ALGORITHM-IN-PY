question:
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers (1's and 0's), representing elements of 2d array a.
4. Consider this array a maze and a player enters from top-left corner in east direction.
5. The player moves in the same direction as long as he meets '0'. On seeing a 1, he takes a 90 deg right turn.
6. You are required to print the indices in (row, col) format of the point from where you exit the matrix.





def matrix(n,m):
    ob=[]
    for i in range(n):
        row=[]
        for  j in range(m):
            row.append(int(input()))
        ob.append(row)
    i=0
    j=0
    dit=0  # 0= east ,1 = south ,2= west, 3=north 
    while(True):
        dit = (dit + ob[i][j]) % 4
        if (dit == 0):
            j+=1 # zero comes then goes diectiion at east and increase the coloumn
        elif(dit == 1):
            i+=1 # if the 1 encounter then goes the direction at the south(turn 90 degree) and increase row
        elif(dit == 2):
            j-=1 # if  1 is encounter again then add with matirx int (dir= dir+ob[i][j]) change the direction into west and decrease column
        elif(dit == 3):
            i-=1 # if  1 is encounter again then add with matirx int (dir= dir+ob[i][j]) change the direction into north and decrease row
            
        #only wnen 1 is encounter then add it with the  previous direction and move into above direction .. don't change the dirction 0 encouters
         
         
         # here we get the enter in the matrix and exit form the matrix
        if (i<0):
            i+=1  # if the row is smaller then zero then exit from the mtirx and print where u before in the matrix
            break
        elif(j<0):
            j+=1 # if the cloumn is smaller then zero then exit from the mtirx and print where  are u before in the matrix
            break
        elif(i == n):
            i-=1 # if the row is bigger or getting out from the loop exit from the mtirx and print where u before in the matrix
            break
        elif(j == m):
            j-=1 # if the column is bigger or getting out from the loop so take  exit from the mtirx and print where u before in the matrix
            break
    
   
    print(i)
    print(j)
   
    
n=int(input())
m=int(input())
matrix(n,m)

>>>>>>

# e= i,j+1
# s=i+1,j
# w=i,j-1
# n=i-1,j
# dir = 0[east]
#       1[south]
#       2[west]
#       3[north]


<>>>>>>>>><><>><><><><><><><><><><><><><><><><><><<><><><><<><><><><><><><><><><><><><><><><><><><><<<><><><><><><>>>>>>>>>>>><><<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>><<<<<<>>>>>><

 input === [[0, 0, 0, 1], [0, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
output =3
        2



