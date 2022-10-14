def matrix(n):
    ob = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        ob.append(row)
    # transpose
    for i, val in enumerate(ob):
        for j in range(i, len(ob[0])):
            val[j], ob[j][i] = ob[j][i], val[j]
    # rotate the matrix
    for i, val in enumerate(ob):
        l = 0
        r = len(ob[0])-1
        while (l <= r):
            val[l], val[r] = val[r], val[l]
            l += 1
            r -= 1
    for i, val in enumerate(ob):
        temp = []
        for j in range(len(ob[0])):
            temp.append(val[j])
        print(" ".join(map(str, temp)))


n = int(input())
matrix(n)

# skipcq
"""
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
"""
