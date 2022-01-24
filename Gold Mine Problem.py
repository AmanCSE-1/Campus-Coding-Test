''' Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. 
    Initially the miner is at first column but can be at any row. He can move only (right->, right up /, right down\) that is from a given cell, 
    the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. 
    Find out maximum amount of gold he can collect. '''


# Python program to solve  Gold Mine problem
MAX = 100

def getMaxGold(gold, m, n):
    ''' Returns maximum amount of gold that can be collected when journey started from first column and moves allowed are right, right-up and right-down'''

	# Create a table for storing intermediate results and initialize all cells to 0.
	# The first row of goldMineTable gives the maximum gold that the miner can collect when starts that row
	goldTable = [[0 for i in range(n)]
						    for j in range(m)]

	for col in range(n-1, -1, -1):
		for row in range(m):

			# Gold collected on going to the cell on the right(->)
			if (col == n-1):
				right = 0
			else:
				right = goldTable[row][col+1]

			# Gold collected on going to the cell to right up (/)
			if (row == 0 or col == n-1):
				right_up = 0
			else:
				right_up = goldTable[row-1][col+1]

			# Gold collected on going to  the cell to right down (\)
			if (row == m-1 or col == n-1):
				right_down = 0
			else:
				right_down = goldTable[row+1][col+1]

			# Max gold collected from taking either of the above 3 paths
			goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)
															
	# The max amount of gold collected will be the max value in first column of all rows
	res = goldTable[0][0]
	for i in range(1, m):
		res = max(res, goldTable[i][0])
	return res
	
if __name__ == "__main__":
    gold = [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]]
 
    m, n = 4, 4

    print(getMaxGold(gold, m, n))
