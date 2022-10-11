# Python3 program for the above approach

# Store direction of all the four
# adjacent cells. We'll move along
# the grid using pairs of values
directionInX = [ -1, 0, 1, 0 ]
directionInY = [ 0, 1, 0, -1 ]

# Function for checking
# if a cell is valid or not
def isValid(x, y, N, M):
	
	if (x < N and x >= 0 and
		y < M and y >= 0):
		return True
		
	return False

# Function which will check whether
# the given array consist of a cycle or not
def isCycle(x, y, arr, visited, parentX, parentY):
	
	# Mark the current vertex as visited
	visited[x][y] = True
	
	N, M = 3, 4
	
	# Loop for generate all possibilities
	# of adjacent cells and checking them
	for k in range(4):
		newX = x + directionInX[k]
		newY = y + directionInY[k]
		
		if (isValid(newX, newY, N, M) and
			arr[newX][newY] == arr[x][y] and
			not (parentX == newX and
					parentY == newY)):
							
			# Check if there exist
			# cycle then return true
			if visited[newX][newY]:
				
				# Return True as the
				# cycle exists
				return True
				
			# If the cycle is not found
			# then keep checking recursively
			else:
				check = isCycle(newX, newY, arr,
								visited, x, y)
				if check:
					return True
					
	# If there was no cycle, taking
	# x and y as source then return false
	return False

# Function to detect Cycle in a grid
def detectCycle(arr):
	
	N, M = 3, 4
	
	# Initially all the cells are unvisited
	visited = [[False] * M for _ in range(N)]

	# Variable to store the result
	cycle = False

	# As there is no fixed position
	# of the cycle we have to loop
	# through all the elements
	for i in range(N):
		
		# If cycle is present and
		# we have already detected
		# it, then break this loop
		if cycle == True:
			break

		for j in range(M):
			
			# Taking (-1, -1) as source
			# node's parent
			if visited[i][j] == False:
				cycle = isCycle(i, j, arr,
								visited, -1, -1)
			
			# If we have encountered a
			# cycle then break this loop
			if cycle == True:
				break
	
	# Cycle was encountered
	if cycle == True:
		print("Yes")
		
	# Cycle was not encountered
	else:
		print("No")

# Driver code
arr = [ [ 'A', 'A', 'A', 'A' ],
		[ 'A', 'B', 'C', 'A' ],
		[ 'A', 'D', 'D', 'A' ] ]

# Function call
detectCycle(arr)
