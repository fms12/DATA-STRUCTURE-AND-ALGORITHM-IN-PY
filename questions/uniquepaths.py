def count_paths(m, n, holes):
    """Return number of paths from (0, 0) to (m, n) in an m x n grid.
 
    holes is a list of tuples (x, y) where each tuple is a coordinate which is
    blocked for a path.
    """
    paths = [[-1]*(m + 1) for _ in range(n + 1)]
 
    if (0, 0) in holes:
        paths[0][0] = 0
    else:
        paths[0][0] = 1
 
    for x in range(1, n + 1):
        if (x, 0) in holes:
            paths[x][0] = 0
        else:
            paths[x][0] = paths[x - 1][0]
 
    for y in range(1, m + 1):
        if (0, y) in holes:
            paths[0][y] = 0
        else:
            paths[0][y] = paths[0][y - 1]
 
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if (x, y) in holes:
                paths[x][y] = 0
            else:
                paths[x][y] = paths[x - 1][y] + paths[x][y - 1]
 
    return paths[n][m]
 
 
m, n = input('Enter m, n for the size of the m x n grid (m rows and n columns): ').split(',')
m = int(m)
n = int(n)
print('Enter the coordinates of holes on each line (empty line to stop): ')
holes = []
while True:
    hole = input('')
    if not hole.strip():
        break
    hole = hole.split(',')
    hole = (int(hole[0]), int(hole[1]))
    holes.append(hole)
 
count = count_paths(m, n, holes)
print('Number of paths from (0, 0) to ({}, {}): {}.'.format(n, m, count))
