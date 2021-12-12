import numpy as np

def adj_finder(matrix, position):
    adj = []
    
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, 10)  # X bounds
            rangeY = range(0, 10)  # Y bounds
            
            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append([newX, newY])
    
    return adj

def array_of_lists_to_array(arr):
    return np.apply_along_axis(lambda a: np.array(a[0]), -1, arr[..., None])

matrix = np.loadtxt('output')

print(matrix.shape)

flashes = 0

for steps in range(0, 2000):
    adjTracker = []
    print("STEP: ", steps + 1)
    for r in range(0, 10):
        for c in range (0, 10):
            # first pass increments one
            matrix[r][c] = int((matrix[r][c])) + 1

            if (matrix[r][c] > 9):
                adj = (adj_finder(matrix, [r,c]))
                adjTracker.extend(adj)
  
    while (len(adjTracker) != 0):
        cur = adjTracker.pop()
        
        if (matrix[cur[0]][cur[1]] <= 9):
            matrix[cur[0]][cur[1]] = int(( matrix[cur[0]][cur[1]] )) + 1

        if ( (matrix[cur[0]][cur[1]] > 9) and (matrix[cur[0]][cur[1]] != 100) ):
            adj = (adj_finder(matrix, [cur[0],cur[1]]))
            adjTracker.extend(adj)

        for r in range(0, 10):
            for c in range (0, 10):
                if (int((matrix[r][c])) > 9):
                    matrix[r][c] = 100

    for r in range(0, 10):
            for c in range (0, 10):
                if (int((matrix[r][c])) > 9):
                    matrix[r][c] = 0

    if (not np.any(matrix)):
        print(steps + 1)
        break
    
print(flashes)