# in the 2X2 grid and only moving right and down there are 6 routes to the bottom 
# how many are there in in a 20X20 grid


# square grid side 
def recPath(gridSize):
    """
    Recursive solution to grid problem. Input is a list of x,y moves remaining.
    """
    # base case, no moves left
    if gridSize == [0,0]: return 1
    # recursive calls
    paths = 0
    # move left when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1, gridSize[1]])
    # move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0], gridSize[1]-1])
    return paths

print(recPath([3, 3]))


def better_recPath(grid):
    path = 1
    for i in range(grid):
        path *= (2*grid)-i
        path /= i+1
    return path 


print(better_recPath(20))


