def matrix(n):
    ob = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        ob.append(row)

    for g in range(len(ob)):
        i = 0
        for j in range(g, len(ob)):
            print(ob[i][j])
            i += 1


n = int(input())
matrix(n)
