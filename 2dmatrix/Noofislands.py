# Python implementation of above approach

# 2D array for the storing the horizontal and vertical
# directions. (Up, left, down, right
dirs = [ [ 0, -1 ],
		[ -1, 0 ],
		[ 0, 1 ],
		[ 1, 0 ] ]

# Function to perform dfs of the input grid
def dfs(grid, x0, y0, i, j, v):
	rows = len(grid)
	cols = len(grid[0])

	if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
		return
	# marking the visited element as -1
	grid[i][j] *= -1

	# computing coordinates with x0, y0 as base
	v.append( (i - x0, j - y0) )

	
	


# Main function that returns distinct count of islands in
# a given boolean 2D matrix
def countDistinctIslands(grid):
	rows = len(grid)
	if rows == 0:
		return 0

	cols = len(grid[0])
	if cols == 0:
		return 0

	coordinates = set()

	for i in range(rows):
		for j in range(cols):

			# If a cell is not 1
			# no need to dfs
			if grid[i][j] != 1:
				continue

			# to hold coordinates
			# of this island
			v = []
			dfs(grid, i, j, i, j, v)

			# insert the coordinates for
			# this island to set
			coordinates.add(tuple(v))
		
	return len(coordinates)

# Driver code
grid = [[ 1, 1, 0, 1, 1 ],
[ 1, 0, 0, 0, 0 ],
[ 0, 0, 0, 0, 1 ],
[ 1, 1, 0, 1, 1 ] ]

print("Number of distinct islands is", countDistinctIslands(grid))
